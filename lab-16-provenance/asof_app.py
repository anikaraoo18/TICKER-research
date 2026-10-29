"""Compare current FRED observations with an ALFRED vintage, no API key needed."""

from datetime import date
from io import StringIO
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st
import altair as alt


SERIES = {
    "BAA": "Moody's Baa corporate bond yield",
    "FEDFUNDS": "Federal funds rate",
    "DGS10": "10-year Treasury yield",
    "MORTGAGE30US": "30-year mortgage rate",
}
FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
ALFRED_CSV = (
    "https://alfred.stlouisfed.org/graph/alfredgraph.csv?"
    "id={series_id}&vintage_date={vintage_date}"
)


def _download_csv(url: str, series_id: str) -> pd.DataFrame:
    """Download and normalize one FRED-family CSV file."""
    request = Request(url, headers={"User-Agent": "asof-learning-demo/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            frame = pd.read_csv(StringIO(response.read().decode("utf-8")))
    except HTTPError as exc:
        raise ValueError(f"FRED could not find {series_id} (HTTP {exc.code}).") from exc
    except URLError as exc:
        raise ValueError(f"Could not download {series_id}: {exc.reason}") from exc
    except Exception as exc:
        raise ValueError(f"Could not read data for {series_id}: {exc}") from exc

    value_columns = [
        column
        for column in frame.columns
        if column == series_id or column.startswith(f"{series_id}_")
    ]
    if "observation_date" not in frame.columns or len(value_columns) != 1:
        raise ValueError(f"FRED returned no usable data for {series_id}.")

    # ALFRED appends the requested vintage date to its value-column name.
    frame = frame[["observation_date", value_columns[0]]].copy()
    frame.columns = ["date", "value"]
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    # FRED and ALFRED use a period to mean that an observation is missing.
    frame["value"] = pd.to_numeric(frame["value"].replace(".", pd.NA), errors="coerce")
    return frame.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)


@st.cache_data(show_spinner=False)
def download_fred(series_id: str) -> pd.DataFrame:
    """Get the current (today's) FRED version of one series."""
    return _download_csv(FRED_CSV.format(series_id=quote(series_id)), series_id)


@st.cache_data(show_spinner=False)
def download_alfred(series_id: str, vintage_date: str) -> pd.DataFrame:
    """Get one series as it was published in the requested ALFRED vintage."""
    return _download_csv(
        ALFRED_CSV.format(series_id=quote(series_id), vintage_date=vintage_date), series_id
    )


def last_observation(frame: pd.DataFrame) -> pd.Series | None:
    """Return the latest non-missing observation, if any."""
    observed = frame.dropna(subset=["value"])
    return None if observed.empty else observed.iloc[-1]


def main() -> None:
    st.set_page_config(page_title="FRED as-of interest rates", layout="wide")
    st.title("Interest rates: current FRED data and an ALFRED vintage")
    st.caption(
        "Data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded "
        "today; built with AI help, a learning demonstration, not investment advice."
    )

    with st.sidebar:
        st.header("Series and dates")
        selected = st.multiselect(
            "Interest-rate series",
            options=list(SERIES),
            default=list(SERIES),
            format_func=lambda series_id: f"{series_id} — {SERIES[series_id]}",
        )
        extra_id = st.text_input("Add another FRED series ID").strip().upper()
        start_date = st.date_input("Start date", value=date(2020, 1, 1))
        as_of_date = st.date_input("As known on", value=date.today())

    series_ids = selected.copy()
    if extra_id and extra_id not in series_ids:
        series_ids.append(extra_id)
    if not series_ids:
        st.info("Choose at least one series or enter a FRED series ID.")
        return

    start_timestamp = pd.Timestamp(start_date)
    vintage_string = as_of_date.isoformat()
    summary_rows = []
    chart_frames = []
    chart_placeholder = st.empty()

    for series_id in series_ids:
        label = SERIES.get(series_id, series_id)
        try:
            with st.spinner(f"Downloading {series_id}..."):
                current = download_fred(series_id)
                vintage = download_alfred(series_id, vintage_string)
        except ValueError as exc:
            st.error(f"{series_id}: {exc}")
            continue

        current_display = current[current["date"] >= start_timestamp]
        chart_frames.append(
            current_display.assign(series=f"{series_id} — {label}")[["date", "value", "series"]]
        )

        vintage_last = last_observation(vintage)
        if vintage_last is None:
            st.caption(f"No non-missing data were known on {as_of_date:%B %-d, %Y}.")
        else:
            st.caption(
                f"Last date in the data known on {as_of_date:%B %-d, %Y}: "
                f"{vintage_last['date']:%Y-%m-%d} ({vintage_last['value']:g})."
            )

        current_last = last_observation(current)
        vintage_date = None if vintage_last is None else vintage_last["date"]
        after_count = (
            0
            if vintage_date is None
            else int(current.loc[current["date"] > vintage_date, "value"].notna().sum())
        )
        matched = vintage.merge(current, on="date", suffixes=("_vintage", "_current"))
        revised_count = int(
            (
                matched["value_vintage"].notna()
                & matched["value_current"].notna()
                & ~matched["value_vintage"].eq(matched["value_current"])
            ).sum()
        )
        summary_rows.append(
            {
                "Series ID": f"https://fred.stlouisfed.org/series/{series_id}",
                "Last measured (as known on)": "—" if vintage_last is None else vintage_last["date"].date(),
                "Value (as known on)": "—" if vintage_last is None else vintage_last["value"],
                "Last measured (today)": "—" if current_last is None else current_last["date"].date(),
                "Value (today)": "—" if current_last is None else current_last["value"],
                "Current values after as-of last date": after_count,
                "Revised values on shared dates": revised_count,
            }
        )

    if chart_frames:
        chart_data = pd.concat(chart_frames, ignore_index=True)
        chart = (
            alt.Chart(chart_data)
            .mark_line()
            .encode(
                x=alt.X(
                    "date:T",
                    title="Date",
                    axis=alt.Axis(format="%b %Y", grid=True),
                ),
                y=alt.Y(
                    "value:Q",
                    title="Percent",
                    scale=alt.Scale(zero=False),
                    axis=alt.Axis(grid=True, labelExpr="datum.label + '%'"),
                ),
                color=alt.Color("series:N", title="Series"),
                tooltip=[
                    alt.Tooltip("date:T", title="Date", format="%Y-%m-%d"),
                    alt.Tooltip("series:N", title="Series"),
                    alt.Tooltip("value:Q", title="Value", format=".4f"),
                ],
            )
            .properties(title="Selected interest-rate series", height=500)
        )
        chart_placeholder.altair_chart(chart, use_container_width=True)

    if summary_rows:
        st.header("Vintage comparison")
        st.caption("“As known on” refers to the ALFRED vintage selected in the sidebar.")
        summary = pd.DataFrame(summary_rows)
        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Series ID": st.column_config.LinkColumn(
                    "Series ID",
                    display_text=r"https://fred\.stlouisfed\.org/series/(.*)",
                ),
                "Value (as known on)": st.column_config.NumberColumn(format="%.4f"),
                "Value (today)": st.column_config.NumberColumn(format="%.4f"),
            },
        )


if __name__ == "__main__":
    main()
