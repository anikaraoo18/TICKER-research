"""One-at-a-time Apple Lab 11 sensitivity analysis (USD millions unless stated)."""

import copy
import sys
from pathlib import Path


LAB10_DIRECTORY = Path(__file__).resolve().parents[1] / "lab-10"
sys.path.insert(0, str(LAB10_DIRECTORY))
import aapl_proforma as model  # noqa: E402


YEARS = model.YEARS
MAC_FY2025_REVENUE = 33_708.0
NON_MAC_FY2025_REVENUE = 382_453.0

# These are independent base inputs. Every run receives a fresh deep copy.
BASE_INPUTS = {
    "revenue_growth": list(model.REVENUE_GROWTH),
    "gross_margin": model.GROSS_MARGIN,
}

MAC_GROWTH_CASES = {
    "Lower": [-0.005, -0.010, -0.015, -0.020, -0.025],
    "Base": [0.045, 0.040, 0.035, 0.030, 0.025],
    "Higher": [0.095, 0.090, 0.085, 0.080, 0.075],
}
GROSS_MARGIN_CASES = {
    "Lower": 0.455,
    "Base": 0.465,
    "Higher": 0.475,
}


def format_path(values):
    """Format annual rate inputs as percentage points."""
    return ", ".join(f"FY{year} {value:.1%}" for year, value in zip(YEARS, values))


def signed_millions(value):
    return f"${value:+,.1f}M"


def signed_per_share(value):
    return f"${value:+,.2f}/share"


def run_model(inputs, mac_growth_path=None):
    """Run Lab 10 with a fresh input copy and return statements plus validation."""
    original_margin = model.GROSS_MARGIN
    model.GROSS_MARGIN = inputs["gross_margin"]
    try:
        projections = []
        opening = copy.deepcopy(model.OPENING)
        mac_revenue = MAC_FY2025_REVENUE
        non_mac_revenue = NON_MAC_FY2025_REVENUE

        for index, year in enumerate(YEARS):
            if mac_growth_path is None:
                total_growth = inputs["revenue_growth"][index]
            else:
                # Only Mac changes here. Non-Mac stays on Lab 10's base path.
                mac_revenue *= 1 + mac_growth_path[index]
                non_mac_revenue *= 1 + inputs["revenue_growth"][index]
                total_revenue = mac_revenue + non_mac_revenue
                total_growth = total_revenue / opening["revenue"] - 1

            projection = model.project_year(year, copy.deepcopy(opening), total_growth)
            projections.append(projection)
            opening = projection

        checks = []
        for year, projection in zip(YEARS, projections):
            model.assert_balanced(year, projection)
            checks.append({
                "year": year,
                "cash_floor_ok": projection["cash"] >= model.CASH_FLOOR,
                "balance_gap": balance_gap(projection),
            })

        valuation_error = None
        try:
            equity_value, terminal_value_share, value_per_share = model.value_equity(projections)
        except ValueError as error:
            equity_value = None
            terminal_value_share = None
            value_per_share = None
            valuation_error = str(error)

        return {
            "valid": True,
            "projections": projections,
            "checks": checks,
            "equity_value": equity_value,
            "terminal_value_share": terminal_value_share,
            "value_per_share": value_per_share,
            "valuation_error": valuation_error,
        }
    except (ValueError, ZeroDivisionError) as error:
        return {
            "valid": False,
            "error": str(error),
            "projections": projections,
            "checks": [],
            "equity_value": None,
            "terminal_value_share": None,
            "value_per_share": None,
            "valuation_error": None,
        }
    finally:
        # The Lab 10 module is restored even if a scenario is invalid.
        model.GROSS_MARGIN = original_margin


def balance_gap(projection):
    """Return the balance-sheet check used by the Lab 10 model."""
    assets = (
        projection["cash"] + projection["marketable_securities"]
        + projection["accounts_receivable"] + projection["vendor_receivables"]
        + projection["inventory"] + projection["other_current_assets"]
        + projection["ppe"] + projection["other_noncurrent_assets"]
    )
    liabilities_and_equity = (
        projection["accounts_payable"] + projection["deferred_revenue"]
        + projection["other_liabilities"] + projection["debt"] + projection["equity"]
    )
    return assets - liabilities_and_equity


def print_checks(result):
    """Keep Lab 10 accounting checks visible for every usable run."""
    print("Accounting checks")
    for check in result["checks"]:
        gap = 0.0 if abs(check["balance_gap"]) < 1e-6 else check["balance_gap"]
        print(
            f"  FY{check['year']}: assets - liabilities - equity = {gap:.1f}; "
            f"cash >= floor: {check['cash_floor_ok']}"
        )


def print_final_year_trace(result):
    """Print the FY2030 linked statement and FCFE details for result tracing."""
    projection = result["projections"][-1]
    print("FY2030 linked statement / FCFE trace (USD millions)")
    for label, key in [
        ("Revenue", "revenue"),
        ("Gross profit", "gross_profit"),
        ("SG&A", "sga"),
        ("Depreciation and amortization", "depreciation"),
        ("Operating profit (EBIT)", "ebit"),
        ("Interest expense", "interest"),
        ("Pretax income", "pretax_income"),
        ("Taxes", "tax"),
        ("Net income", "net_income"),
        ("Capital spending", "capex"),
        ("Change in accounts receivable", "change_in_ar"),
        ("Change in vendor receivables", "change_in_vendor_receivables"),
        ("Change in inventory", "change_in_inventory"),
        ("Change in other current assets", "change_in_other_current_assets"),
        ("Change in other non-current assets", "change_in_other_noncurrent_assets"),
        ("Change in accounts payable", "change_in_ap"),
        ("Change in deferred revenue", "change_in_deferred_revenue"),
        ("Change in other liabilities", "change_in_other_liabilities"),
        ("FCFE before share repurchases", "fcfe"),
    ]:
        print(f"  {label:<38}{projection[key]:>14,.1f}")


def print_run(driver, case, inputs, result, mac_growth_path=None):
    """Print actual inputs, final outputs, checks, and trace details for one run."""
    print(f"\n{driver} — {case} case")
    if mac_growth_path is not None:
        print(f"  Mac revenue growth (percentage points): {format_path(mac_growth_path)}")
        print(
            "  Non-Mac revenue growth, held at base (percentage points): "
            f"{format_path(inputs['revenue_growth'])}"
        )
        print(
            "  Gross margin, held at base (percentage points of revenue): "
            f"FY2026-FY2030 {inputs['gross_margin']:.1%}"
        )
    else:
        print(
            "  Gross margin (percentage points of revenue): "
            f"FY2026-FY2030 {inputs['gross_margin']:.1%}"
        )
        print(
            "  Mac revenue growth, held at base (percentage points): "
            f"{format_path(inputs['revenue_growth'])}"
        )
        print(
            "  Non-Mac revenue growth, held at base (percentage points): "
            f"{format_path(inputs['revenue_growth'])}"
        )

    if not result["valid"]:
        print(f"  INVALID RUN: {result['error']}")
        return

    final_year = result["projections"][-1]
    print(f"  FY2030 operating profit (EBIT): ${final_year['ebit']:,.1f}M")
    print(f"  FY2030 FCFE before share repurchases: ${final_year['fcfe']:,.1f}M")
    if result["value_per_share"] is None:
        print(f"  Value per fixed diluted share: unavailable ({result['valuation_error']})")
        print("  Signed FCFE is retained because valuation is unavailable.")
    else:
        print(f"  Value per fixed diluted share: ${result['value_per_share']:,.2f}")
    print_checks(result)
    print_final_year_trace(result)


def metrics(result):
    """Return comparable outputs only for usable runs."""
    if not result["valid"]:
        return None
    final_year = result["projections"][-1]
    return {
        "operating_profit": final_year["ebit"],
        "fcfe": final_year["fcfe"],
        "value_per_share": result["value_per_share"],
    }


def print_comparison(driver, scenarios):
    """Report signed changes from base and spans without ranking scenarios."""
    base_metrics = metrics(scenarios["Base"])
    print(f"\n{driver} — comparison with base")
    if base_metrics is None:
        print("  Base run is invalid; signed comparisons and spans are unavailable.")
        return

    print(
        f"{'Case':<10}{'FY2030 operating profit Δ':>30}"
        f"{'FY2030 FCFE Δ':>22}{'Value/share Δ':>20}"
    )
    valid_metrics = []
    for case in ("Lower", "Base", "Higher"):
        scenario_metrics = metrics(scenarios[case])
        if scenario_metrics is None:
            print(f"{case:<10}{'INVALID RUN':>30}")
            continue
        valid_metrics.append(scenario_metrics)
        operating_change = scenario_metrics["operating_profit"] - base_metrics["operating_profit"]
        fcfe_change = scenario_metrics["fcfe"] - base_metrics["fcfe"]
        if scenario_metrics["value_per_share"] is None or base_metrics["value_per_share"] is None:
            value_change = "unavailable"
        else:
            value_change = signed_per_share(
                scenario_metrics["value_per_share"] - base_metrics["value_per_share"]
            )
        print(
            f"{case:<10}{signed_millions(operating_change):>30}"
            f"{signed_millions(fcfe_change):>22}{value_change:>20}"
        )

    if not valid_metrics:
        print("  No valid runs are available for output spans.")
        return
    operating_span = max(item["operating_profit"] for item in valid_metrics) - min(
        item["operating_profit"] for item in valid_metrics
    )
    fcfe_span = max(item["fcfe"] for item in valid_metrics) - min(
        item["fcfe"] for item in valid_metrics
    )
    values = [item["value_per_share"] for item in valid_metrics if item["value_per_share"] is not None]
    print(f"  Output span — FY2030 operating profit: ${operating_span:,.1f}M")
    print(f"  Output span — FY2030 FCFE: ${fcfe_span:,.1f}M")
    if values:
        print(f"  Output span — value per fixed diluted share: ${max(values) - min(values):,.2f}")
    else:
        print("  Output span — value per fixed diluted share: unavailable")


def print_base_comparison(initial_result, restored_result):
    """Show that the original base output is reproduced before and after analysis."""
    initial_metrics = metrics(initial_result)
    restored_metrics = metrics(restored_result)
    print("\nRestored-base comparison")
    if initial_metrics is None or restored_metrics is None:
        print("  Base comparison unavailable because a base run is invalid.")
        return
    print(
        f"  FY2030 operating profit: initial ${initial_metrics['operating_profit']:,.1f}M; "
        f"restored ${restored_metrics['operating_profit']:,.1f}M; "
        f"difference {signed_millions(restored_metrics['operating_profit'] - initial_metrics['operating_profit'])}"
    )
    print(
        f"  FY2030 FCFE: initial ${initial_metrics['fcfe']:,.1f}M; "
        f"restored ${restored_metrics['fcfe']:,.1f}M; "
        f"difference {signed_millions(restored_metrics['fcfe'] - initial_metrics['fcfe'])}"
    )
    if initial_metrics["value_per_share"] is not None and restored_metrics["value_per_share"] is not None:
        print(
            f"  Value per fixed diluted share: initial ${initial_metrics['value_per_share']:,.2f}; "
            f"restored ${restored_metrics['value_per_share']:,.2f}; "
            f"difference {signed_per_share(restored_metrics['value_per_share'] - initial_metrics['value_per_share'])}"
        )


def main():
    print("Apple Lab 11 one-at-a-time sensitivity analysis")
    print("All dollar amounts are USD millions unless stated otherwise.")
    print("FCFE is free cash flow to equity before share repurchases.")

    # Original Lab 10 base: shown before any sensitivity run.
    initial_base_inputs = copy.deepcopy(BASE_INPUTS)
    initial_base = run_model(initial_base_inputs)
    print_run("Original Lab 10 base", "Base", initial_base_inputs, initial_base)

    mac_scenarios = {}
    for case, mac_path in MAC_GROWTH_CASES.items():
        inputs = copy.deepcopy(BASE_INPUTS)
        result = run_model(inputs, mac_path)
        mac_scenarios[case] = result
        print_run("Driver 1: Mac revenue growth", case, inputs, result, mac_path)
    print_comparison("Driver 1: Mac revenue growth", mac_scenarios)

    margin_scenarios = {}
    for case, gross_margin in GROSS_MARGIN_CASES.items():
        inputs = copy.deepcopy(BASE_INPUTS)
        inputs["gross_margin"] = gross_margin
        result = run_model(inputs)
        margin_scenarios[case] = result
        print_run("Driver 2: Gross margin", case, inputs, result)
    print_comparison("Driver 2: Gross margin", margin_scenarios)

    # A fresh base copy is used after all runs; Lab 10 globals are already restored.
    restored_base_inputs = copy.deepcopy(BASE_INPUTS)
    restored_base = run_model(restored_base_inputs)
    print_run("Restored Lab 10 base", "Base", restored_base_inputs, restored_base)
    print_base_comparison(initial_base, restored_base)


if __name__ == "__main__":
    main()
