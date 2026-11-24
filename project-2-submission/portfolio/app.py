"""Streamlit learning demonstration for Lab 15's Meridian portfolio exercise."""

from __future__ import annotations

import csv
from io import StringIO

import streamlit as st

from portfolio import (
    CORRELATIONS,
    EXPECTED_RETURNS,
    RESERVE_ELIGIBLE_SLEEVES,
    SLEEVES,
    VOLATILITIES,
    estimate_annual_inputs_from_csv,
    find_lowest_volatility_mix,
)


MERIDIAN_RESERVE_TICKERS = {"SGOV", "VGIT"}
BASE_OBJECTIVE_PERCENT = 6.5
BASE_RESERVE_PERCENT = 3.0
DRIVER_MIN_PERCENT = -25.0
DRIVER_MAX_PERCENT = 25.0

DOCUMENTED_ALLOCATION_ROWS = [
    {"Scenario": "60-month base", "Asset": "SGOV", "Weight": 65.0},
    {"Scenario": "60-month base", "Asset": "VGIT", "Weight": 0.0},
    {"Scenario": "60-month base", "Asset": "VCIT", "Weight": 0.0},
    {"Scenario": "60-month base", "Asset": "VTI", "Weight": 35.0},
    {"Scenario": "36-month lookback", "Asset": "SGOV", "Weight": 85.0},
    {"Scenario": "36-month lookback", "Asset": "VGIT", "Weight": 0.0},
    {"Scenario": "36-month lookback", "Asset": "VCIT", "Weight": 0.0},
    {"Scenario": "36-month lookback", "Asset": "VTI", "Weight": 15.0},
    {"Scenario": "7.00% objective", "Asset": "SGOV", "Weight": 60.0},
    {"Scenario": "7.00% objective", "Asset": "VGIT", "Weight": 0.0},
    {"Scenario": "7.00% objective", "Asset": "VCIT", "Weight": 0.0},
    {"Scenario": "7.00% objective", "Asset": "VTI", "Weight": 40.0},
]


def validate_uploaded_csv_shape(csv_text: str) -> None:
    """Reject malformed CSV rows before estimating portfolio inputs."""
    rows = csv.reader(StringIO(csv_text))
    try:
        header = next(rows)
    except StopIteration as error:
        raise ValueError("CSV is empty.") from error
    if not header or header[0] != "Date":
        raise ValueError("CSV must have Date as its first column.")
    if not 3 <= len(header) - 1 <= 6:
        raise ValueError("CSV must contain between 3 and 6 ticker columns after Date.")
    if any(len(row) != len(header) for row in rows):
        raise ValueError("CSV contains a row with a different number of columns than its header.")


def validate_uploaded_estimates(estimates: dict[str, object]) -> tuple[str, ...]:
    """Confirm that the uploaded CSV has a usable, dynamic ticker universe."""
    tickers = tuple(estimates["tickers"])
    if not 3 <= len(tickers) <= 6:
        raise ValueError("CSV must contain between 3 and 6 ticker columns after Date.")
    if len(set(tickers)) != len(tickers):
        raise ValueError("CSV ticker column names must be unique.")
    return tickers


def show_mix(label: str, assets: tuple[str, ...], mix: dict[str, object] | None) -> None:
    """Show one grid-search result using two-decimal percentage formatting."""
    st.subheader(label)
    if mix is None:
        st.write("no mix meets the objective")
        return
    weights = mix["weights"]
    st.table(
        {
            "Asset": list(assets),
            "Weight": [f"{weights[asset]:.2%}" for asset in assets],
        }
    )
    st.write(f"Expected return: {mix['expected_return']:.2%}")
    st.write(f"Volatility: {mix['volatility']:.2%}")
    st.write(f"Reserve-eligible weight: {mix['reserve_eligible_weight']:.2%}")


def reset_to_loaded_base_case(
    assets: tuple[str, ...],
    expected_returns: dict[str, float],
    default_reserve_eligible: set[str],
) -> None:
    """Restore the app's documented base-case scenario controls."""
    st.session_state["objective-input"] = BASE_OBJECTIVE_PERCENT
    st.session_state["reserve-minimum-input"] = BASE_RESERVE_PERCENT
    st.session_state["use-last-36-months"] = False
    for asset in assets:
        st.session_state[f"expected-return-{asset}"] = expected_returns[asset] * 100.0
        st.session_state[f"reserve-eligible-{asset}"] = asset in default_reserve_eligible


st.set_page_config(page_title="Project 2 Portfolio Analysis", layout="wide")
st.title("Project 2 Portfolio Decision Summary")
st.caption("Educational portfolio analysis only; not investment advice.")

st.subheader("Mandate and current panel status")
st.markdown(
    "- **Objective:** 6.50% annual return hurdle; normal-case results are not "
    "separately cost-adjusted.\n"
    "- **Reserve minimum:** 3.00%.\n"
    "- **Process:** long-only grid search in 5-percentage-point steps.\n"
    "- **Unresolved issue:** the 10% calendar-year loss-rule definition is not set."
)
st.subheader("Mandate constraint status")
st.markdown(
    "- **Modeled:** 6.50% annual return hurdle, 3.00% reserve minimum, and a "
    "long-only search. The 0.25-percentage-point implementation-cost "
    "deduction is used only in the downside stress test.\n"
    "- **Not certified by this classroom app:** the $3 million distribution "
    "reserve because portfolio value is unknown; issuer cap; turnover limit; "
    "five-business-day liquidity; no-derivatives/no-borrowing implementation "
    "controls; and the unresolved 10% calendar-year loss-rule definition."
)
st.error(
    "**Do not allocate or rebalance yet.** The 10% loss rule is unresolved, "
    "the allocation is sensitive to the historical lookback window, and the "
    "locked downside stress test produced no qualifying portfolio."
)

st.subheader("Committee adoption gates")
st.caption(
    "This is a governance view of documented evidence, not a new score or a new optimization. "
    "A mechanically qualifying base-case mix alone cannot authorize a trade."
)
st.markdown(
    "| Adoption gate | Current evidence | Status | Committee implication |\n"
    "|---|---|---|---|\n"
    "| Base mechanical fit | 60-month result meets the modeled 6.50% hurdle and 3.00% reserve minimum. | Met | Necessary, but not sufficient for adoption. |\n"
    "| Allocation stability | Changing only the lookback moved the allocation by 20 percentage points. | Unresolved | Do not treat one historical window as a durable instruction. |\n"
    "| Downside resilience | Locked -25% VTI stress test produced no qualifying portfolio. | Not met | Stop condition: do not allocate; escalate. |\n"
    "| Governance | The 10% calendar-year loss rule has no defined enforcement convention. | Unresolved | CIO clarification is required before adoption. |\n"
    "| Point-in-time provenance | Saved snapshot is documented, but unrevised historical availability is not proven. | Needs confirmation | Keep BAA10YM quarantined and confirm data governance. |"
)

st.subheader("Allocation stability across documented scenarios")
st.caption(
    "These are already recorded Project 2 results. The chart does not run a new optimization or "
    "forecast returns; it makes the documented allocation changes visible for committee review."
)
st.vega_lite_chart(
    DOCUMENTED_ALLOCATION_ROWS,
    {
        "mark": {"type": "bar"},
        "encoding": {
            "y": {
                "field": "Scenario",
                "type": "nominal",
                "sort": ["60-month base", "36-month lookback", "7.00% objective"],
                "title": None,
            },
            "x": {
                "field": "Weight",
                "type": "quantitative",
                "stack": "zero",
                "scale": {"domain": [0, 100]},
                "axis": {"title": "Portfolio weight (%)", "format": ".0f"},
            },
            "color": {"field": "Asset", "type": "nominal", "title": "ETF sleeve"},
            "tooltip": [
                {"field": "Scenario", "type": "nominal"},
                {"field": "Asset", "type": "nominal"},
                {"field": "Weight", "type": "quantitative", "format": ".2f", "title": "Weight (%)"},
            ],
        },
    },
    use_container_width=True,
)

st.subheader("Lab 14 baselines")
st.caption(
    "These are comparative classroom baselines using the original four sleeves, "
    "not allocations in the active SGOV/VGIT/VCIT/VTI ETF universe."
)
st.markdown(
    "| Baseline | Verified four-sleeve weights | Expected return | Volatility | "
    "Reserve-eligible weight | Mandate verdict |\n"
    "|---|---|---:|---:|---:|---|\n"
    "| Benchmark | Treasury bills 0%; Treasury 10-year note 0%; "
    "investment-grade bond fund 40%; global equity index fund 60% | 6.80% | "
    "10.46% | 0.00% | Meets the 6.5% objective but fails the 3.00% reserve "
    "minimum; not approved. |\n"
    "| Equal weight | Treasury bills 25%; Treasury 10-year note 25%; "
    "investment-grade bond fund 25%; global equity index fund 25% | 5.20% | "
    "5.21% | 50.00% | Meets the reserve minimum but misses the 6.5% objective; "
    "not approved. |"
)

st.subheader("Documented Project 2 results")
st.markdown(
    "- **60-month constrained SGOV/VGIT/VCIT/VTI result:** SGOV 65%; VGIT 0%; "
    "VCIT 0%; VTI 35%; 6.62% expected return; 5.64% volatility; 65% "
    "reserve-eligible weight. **Conditionally qualifying mechanically; not "
    "approved for allocation.**\n"
    "- **Locked 36-month comparison:** SGOV 85%; VGIT 0%; VCIT 0%; VTI 15%; "
    "7.06% expected return; 1.99% volatility. The largest allocation change "
    "was 20 percentage points.\n"
    "- **Lab 20 objective comparison:** Raising only the objective from 6.50% "
    "to 7.00% produced SGOV 60% / VTI 40%; 7.03% expected return; 6.42% "
    "volatility; and 60% reserve-eligible weight. The largest allocation "
    "change was 5 percentage points; the defer decision stayed the same.\n"
    "- **Downside stress test:** No qualifying portfolio—do not allocate; "
    "escalate for CIO guidance."
)

st.subheader("Point-in-time and provenance notice")
st.info(
    "The saved price snapshot ends September 2026 and was retrieved October "
    "22, 2026. Historical estimates are not forecasts. BAA10YM is quarantined "
    "and is not a decision input."
)
st.caption(
    "AI-use disclosure: Codex helped format this interface from documented "
    "repository evidence; the student retains responsibility for whether to "
    "use the displayed information."
)

st.divider()
st.header("Meridian Lab 15 Portfolio Explorer")
st.write("Built with AI help, a learning demonstration, not investment advice.")

with st.sidebar:
    st.header("Inputs")
    objective = st.number_input(
        "Objective (%)", 0.0, 15.0, BASE_OBJECTIVE_PERCENT, 0.1, key="objective-input"
    ) / 100.0
    reserve_minimum = st.number_input(
        "Reserve minimum (%)", 0.0, 100.0, BASE_RESERVE_PERCENT, 0.1,
        key="reserve-minimum-input"
    ) / 100.0
    uploaded_file = st.file_uploader("Upload prices.csv", type="csv")
    use_last_36_months = st.toggle("Use last 36 months", value=False, key="use-last-36-months")

csv_all_months: dict[str, object] | None = None
csv_active_months: dict[str, object] | None = None
assets = SLEEVES
if uploaded_file is not None:
    try:
        csv_text = uploaded_file.getvalue().decode("utf-8")
        validate_uploaded_csv_shape(csv_text)
        csv_all_months = estimate_annual_inputs_from_csv(StringIO(csv_text))
        assets = validate_uploaded_estimates(csv_all_months)
        csv_active_months = estimate_annual_inputs_from_csv(
            StringIO(csv_text), last_36_months=use_last_36_months
        )
        if tuple(csv_active_months["tickers"]) != assets:
            raise ValueError("CSV ticker columns changed while estimating inputs.")
    except (UnicodeDecodeError, ValueError, TypeError, csv.Error) as error:
        st.error(f"Could not use the uploaded CSV: {error}")
        st.stop()

meridian_inputs = {
    "expected_returns": EXPECTED_RETURNS,
    "volatilities": VOLATILITIES,
    "correlations": CORRELATIONS,
}
active_inputs = csv_active_months or meridian_inputs
loaded_inputs = csv_all_months or meridian_inputs

st.subheader("Editable expected returns")
st.caption(
    "Scenario controls are educational what-if inputs, not forecasts. Expected-return "
    "drivers are bounded from -25% to 25%; use Reset to return to the documented base case."
)
editable_returns: dict[str, float] = {}
input_columns = st.columns(len(assets))
for column, asset in zip(input_columns, assets):
    with column:
        editable_returns[asset] = (
            st.number_input(
                asset,
                min_value=DRIVER_MIN_PERCENT,
                max_value=DRIVER_MAX_PERCENT,
                value=float(active_inputs["expected_returns"][asset] * 100.0),
                step=0.1,
                key=f"expected-return-{asset}",
            )
            / 100.0
        )

st.subheader("Reserve eligibility")
eligible_sleeves = {
    asset
    for asset in assets
    if st.checkbox(
        asset,
        value=(
            asset in MERIDIAN_RESERVE_TICKERS
            if csv_active_months is not None
            else asset in RESERVE_ELIGIBLE_SLEEVES
        ),
        key=f"reserve-eligible-{asset}",
    )
}

default_reserve_eligible = (
    MERIDIAN_RESERVE_TICKERS if csv_active_months is not None else RESERVE_ELIGIBLE_SLEEVES
)
st.button(
    "Reset to loaded base case",
    on_click=reset_to_loaded_base_case,
    args=(assets, active_inputs["expected_returns"], default_reserve_eligible),
)

selected_mix = find_lowest_volatility_mix(
    assets,
    editable_returns,
    active_inputs["volatilities"],
    active_inputs["correlations"],
    objective,
    reserve_minimum,
    eligible_sleeves,
)
loaded_mix = find_lowest_volatility_mix(
    assets,
    loaded_inputs["expected_returns"],
    loaded_inputs["volatilities"],
    loaded_inputs["correlations"],
    objective,
    reserve_minimum,
    eligible_sleeves,
)

left, right = st.columns(2)
with left:
    show_mix("Lowest-risk qualifying mix", assets, selected_mix)
with right:
    source_label = "CSV estimates using all months" if csv_all_months else "Meridian inputs"
    show_mix(f"Loaded-input answer ({source_label})", assets, loaded_mix)

if selected_mix is None or loaded_mix is None:
    st.write("Largest weight change: unavailable because at least one result has no qualifying mix.")
else:
    largest_change = max(
        abs(selected_mix["weights"][sleeve] - loaded_mix["weights"][sleeve])
        for sleeve in assets
    )
    st.write(f"Largest weight change: {largest_change * 100.0:.2f} percentage points")
