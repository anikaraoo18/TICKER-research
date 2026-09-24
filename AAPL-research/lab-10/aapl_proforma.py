"""Apple FY2026-FY2030 three-statement model and FCFE valuation (USD millions)."""

# Editable inputs — sourced from AAPL-research/lab-10/aapl_lab10_assumptions.md.
YEARS = [2026, 2027, 2028, 2029, 2030]
REVENUE_GROWTH = [0.045, 0.040, 0.035, 0.030, 0.025]
GROSS_MARGIN = 0.465
SGA_TO_GROSS_PROFIT = 0.144
INVENTORY_DAYS = 11.0
DA_TO_OPENING_NET_PPE = 0.250
CAPEX_TO_REVENUE = 0.030
TAX_RATE = 0.170
CASH_FLOOR = 30_000.0
MARKETABLE_SECURITIES = 96_486.0
TOTAL_DEBT = 98_657.0
DEBT_INTEREST_RATE = 0.045
FIXED_DILUTED_SHARES = 15_004.697
COST_OF_EQUITY = 0.100
TERMINAL_GROWTH = 0.025

# FY2025 operating-balance conventions documented in the Lab 10 assumptions.
AR_TO_REVENUE = 0.096
VENDOR_RECEIVABLES_TO_REVENUE = 0.080
INVENTORY_TO_REVENUE = 0.014
OTHER_CURRENT_ASSETS_TO_REVENUE = 0.035
OTHER_NONCURRENT_ASSETS_TO_REVENUE = 0.201
AP_TO_REVENUE = 0.168
DEFERRED_REVENUE_TO_REVENUE = 0.022
OTHER_LIABILITIES_TO_REVENUE = 0.259

OPENING = {
    "revenue": 416_161.0,
    "cash": 35_934.0,
    "marketable_securities": MARKETABLE_SECURITIES,
    "accounts_receivable": 39_777.0,
    "vendor_receivables": 33_180.0,
    "inventory": 5_718.0,
    "other_current_assets": 14_585.0,
    "ppe": 49_834.0,
    "other_noncurrent_assets": 83_727.0,
    "accounts_payable": 69_860.0,
    "deferred_revenue": 9_055.0,
    "other_liabilities": 107_936.0,
    "debt": TOTAL_DEBT,
    "equity": 73_733.0,
}


def assert_balanced(year, projection):
    """Raise an error that identifies the fiscal year and balance-sheet gap."""
    assets = (
        projection["cash"] + projection["marketable_securities"]
        + projection["accounts_receivable"] + projection["vendor_receivables"]
        + projection["inventory"] + projection["other_current_assets"]
        + projection["ppe"] + projection["other_noncurrent_assets"]
    )
    liabilities_equity = (
        projection["accounts_payable"] + projection["deferred_revenue"]
        + projection["other_liabilities"] + projection["debt"] + projection["equity"]
    )
    gap = assets - liabilities_equity
    if abs(gap) > 1e-6:
        raise ValueError(f"FY{year}: balance-sheet gap is {gap:.6f}")
    if projection["cash"] < CASH_FLOOR - 1e-6:
        shortfall = CASH_FLOOR - projection["cash"]
        raise ValueError(f"FY{year}: cash is below the ${CASH_FLOOR:,.1f} floor by {shortfall:,.1f}")


def project_year(year, opening, revenue_growth):
    """Project one fiscal year; FCFE is calculated before share repurchases."""
    p = {}
    p["revenue"] = opening["revenue"] * (1 + revenue_growth)
    p["gross_profit"] = p["revenue"] * GROSS_MARGIN
    p["cost_of_sales"] = p["revenue"] - p["gross_profit"]
    p["sga"] = p["gross_profit"] * SGA_TO_GROSS_PROFIT
    p["depreciation"] = opening["ppe"] * DA_TO_OPENING_NET_PPE
    p["ebit"] = p["gross_profit"] - p["sga"] - p["depreciation"]
    p["interest"] = opening["debt"] * DEBT_INTEREST_RATE
    p["pretax_income"] = p["ebit"] - p["interest"]
    p["tax"] = max(0.0, p["pretax_income"]) * TAX_RATE
    p["net_income"] = p["pretax_income"] - p["tax"]

    p["accounts_receivable"] = p["revenue"] * AR_TO_REVENUE
    p["vendor_receivables"] = p["revenue"] * VENDOR_RECEIVABLES_TO_REVENUE
    p["inventory"] = p["cost_of_sales"] * INVENTORY_DAYS / 365
    p["other_current_assets"] = p["revenue"] * OTHER_CURRENT_ASSETS_TO_REVENUE
    p["capex"] = p["revenue"] * CAPEX_TO_REVENUE
    p["ppe"] = opening["ppe"] + p["capex"] - p["depreciation"]
    p["other_noncurrent_assets"] = p["revenue"] * OTHER_NONCURRENT_ASSETS_TO_REVENUE
    p["marketable_securities"] = MARKETABLE_SECURITIES

    p["accounts_payable"] = p["revenue"] * AP_TO_REVENUE
    p["deferred_revenue"] = p["revenue"] * DEFERRED_REVENUE_TO_REVENUE
    p["other_liabilities"] = p["revenue"] * OTHER_LIABILITIES_TO_REVENUE
    p["debt"] = TOTAL_DEBT

    p["change_in_ar"] = p["accounts_receivable"] - opening["accounts_receivable"]
    p["change_in_vendor_receivables"] = p["vendor_receivables"] - opening["vendor_receivables"]
    p["change_in_inventory"] = p["inventory"] - opening["inventory"]
    p["change_in_other_current_assets"] = p["other_current_assets"] - opening["other_current_assets"]
    p["change_in_other_noncurrent_assets"] = p["other_noncurrent_assets"] - opening["other_noncurrent_assets"]
    p["change_in_ap"] = p["accounts_payable"] - opening["accounts_payable"]
    p["change_in_deferred_revenue"] = p["deferred_revenue"] - opening["deferred_revenue"]
    p["change_in_other_liabilities"] = p["other_liabilities"] - opening["other_liabilities"]

    p["fcfe"] = (
        p["net_income"] + p["depreciation"] - p["capex"]
        - p["change_in_ar"] - p["change_in_vendor_receivables"]
        - p["change_in_inventory"] - p["change_in_other_current_assets"]
        - p["change_in_other_noncurrent_assets"] + p["change_in_ap"]
        + p["change_in_deferred_revenue"] + p["change_in_other_liabilities"]
    )
    p["cash_before_repurchases"] = opening["cash"] + p["fcfe"]
    if p["cash_before_repurchases"] < CASH_FLOOR - 1e-6:
        shortfall = CASH_FLOOR - p["cash_before_repurchases"]
        raise ValueError(
            f"FY{year}: cash before share repurchases is below the "
            f"${CASH_FLOOR:,.1f} floor by {shortfall:,.1f}"
        )
    p["share_repurchases"] = max(0.0, p["cash_before_repurchases"] - CASH_FLOOR)
    p["cash"] = p["cash_before_repurchases"] - p["share_repurchases"]
    p["equity"] = opening["equity"] + p["net_income"] - p["share_repurchases"]
    return p


def print_table(title, rows, projections):
    """Print a one-decimal table with fiscal years across columns."""
    print(f"\n{title} (USD millions)")
    print(f"{'':<42}" + "".join(f"{'FY' + str(year):>12}" for year in YEARS))
    print("-" * 102)
    for label, key in rows:
        print(f"{label:<42}" + "".join(f"{p[key]:>12,.1f}" for p in projections))


def value_equity(projections):
    """Value FCFE before share repurchases using a Gordon-growth terminal value."""
    if TERMINAL_GROWTH >= COST_OF_EQUITY:
        raise ValueError("Terminal growth must be below the cost of equity.")
    pv_fcfe = sum(
        p["fcfe"] / (1 + COST_OF_EQUITY) ** year
        for year, p in enumerate(projections, start=1)
    )
    terminal_value = (
        projections[-1]["fcfe"] * (1 + TERMINAL_GROWTH)
        / (COST_OF_EQUITY - TERMINAL_GROWTH)
    )
    pv_terminal_value = terminal_value / (1 + COST_OF_EQUITY) ** len(projections)
    equity_value = pv_fcfe + pv_terminal_value
    return equity_value, pv_terminal_value / equity_value, equity_value / FIXED_DILUTED_SHARES


def main():
    projections = []
    opening = OPENING.copy()
    for year, growth in zip(YEARS, REVENUE_GROWTH):
        projection = project_year(year, opening, growth)
        projections.append(projection)
        opening = projection

    print("Apple FY2026-FY2030 three-statement model")
    print("Simplifications: marketable securities are held constant at $96,486.0 million.")
    print("Simplifications: diluted shares are fixed at 15,004.697 million for valuation.")
    print("Share repurchases deploy cash above the $30,000.0 million cash floor.")

    print_table("Income Statement", [
        ("Revenue", "revenue"), ("Cost of sales", "cost_of_sales"),
        ("Gross profit", "gross_profit"), ("SG&A", "sga"),
        ("Depreciation and amortization", "depreciation"),
        ("EBIT", "ebit"), ("Interest expense", "interest"),
        ("Pretax income", "pretax_income"), ("Taxes", "tax"),
        ("Net income", "net_income"),
    ], projections)
    print_table("Balance Sheet", [
        ("Cash and cash equivalents", "cash"),
        ("Marketable securities", "marketable_securities"),
        ("Accounts receivable", "accounts_receivable"),
        ("Vendor non-trade receivables", "vendor_receivables"),
        ("Inventory", "inventory"), ("Other current assets", "other_current_assets"),
        ("Net PP&E", "ppe"), ("Other non-current assets", "other_noncurrent_assets"),
        ("Accounts payable", "accounts_payable"),
        ("Deferred revenue", "deferred_revenue"),
        ("Other liabilities", "other_liabilities"), ("Total debt", "debt"),
        ("Shareholders' equity", "equity"),
    ], projections)
    print_table("Cash Flow / FCFE", [
        ("Net income", "net_income"), ("Depreciation and amortization", "depreciation"),
        ("Capital spending", "capex"), ("Change in accounts receivable", "change_in_ar"),
        ("Change in vendor receivables", "change_in_vendor_receivables"),
        ("Change in inventory", "change_in_inventory"),
        ("Change in other current assets", "change_in_other_current_assets"),
        ("Change in other non-current assets", "change_in_other_noncurrent_assets"),
        ("Change in accounts payable", "change_in_ap"),
        ("Change in deferred revenue", "change_in_deferred_revenue"),
        ("Change in other liabilities", "change_in_other_liabilities"),
        ("FCFE before share repurchases", "fcfe"),
        ("Share repurchases", "share_repurchases"),
        ("Ending cash", "cash"),
    ], projections)

    print("\nChecks")
    for year, projection in zip(YEARS, projections):
        assert_balanced(year, projection)
        assets = (
            projection["cash"] + projection["marketable_securities"]
            + projection["accounts_receivable"] + projection["vendor_receivables"]
            + projection["inventory"] + projection["other_current_assets"]
            + projection["ppe"] + projection["other_noncurrent_assets"]
        )
        liabilities_equity = (
            projection["accounts_payable"] + projection["deferred_revenue"]
            + projection["other_liabilities"] + projection["debt"] + projection["equity"]
        )
        gap = assets - liabilities_equity
        display_gap = 0.0 if abs(gap) < 1e-6 else gap
        print(
            f"FY{year}: assets - liabilities - equity = {display_gap:.1f}; "
            f"cash >= floor: {projection['cash'] >= CASH_FLOOR}"
        )

    equity_value, terminal_share, value_per_share = value_equity(projections)
    print(f"\nEquity value: {equity_value:,.2f}")
    print(f"Terminal-value share of total value: {terminal_share:.2%}")
    print(f"Value per share: {value_per_share:,.2f}")


if __name__ == "__main__":
    main()
