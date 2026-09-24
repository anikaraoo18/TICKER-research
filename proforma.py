"""Five-year three-statement projection and FCFE valuation (USD millions)."""

YEARS = [2026, 2027, 2028, 2029, 2030]
REVENUE_GROWTH, GROSS_MARGIN = 0.018, 0.1705
SGA_RATIOS = [0.665, 0.655, 0.645, 0.645, 0.645]
DEPR_RATIO = 82.4 / 3_070.4
IMPAIRMENT, CAPEX, TAX_RATE = 120.0, 250.0, 0.255
INVENTORY_DAYS = 2_135.8 / (17_999.0 - 3_071.7) * 365
FLOOR_PLAN_RATIO, OWC_RATE = 2_027.0 / 2_135.8, 0.008
MIN_CASH, REVOLVER_LIMIT, REVOLVER_RATE = 25.0, 850.0, 0.06
REPAYMENT, BUYBACK = 150.0, 150.0
FLOOR_PLAN_RATE, TERM_DEBT_RATE = 0.0467, 0.0544
COST_OF_EQUITY, TERMINAL_GROWTH, SHARES = 0.10, 0.025, 17.951349

OPENING = {
    "revenue": 17_999.0, "inventory": 2_135.8, "ppe": 3_070.4,
    "other_assets": 6_371.6, "cash": 40.4, "floor_plan": 2_027.0,
    "term_debt": 3_572.0, "revolver": 0.0, "other_liabilities": 2_127.5,
    "equity": 3_891.7,
}


def assert_balanced(year, p):
    """Raise an informative error for a balance-sheet or cash-minimum failure."""
    assets = p["inventory"] + p["ppe"] + p["other_assets"] + p["cash"]
    liabilities_equity = (p["floor_plan"] + p["term_debt"] + p["revolver"]
                          + p["other_liabilities"] + p["equity"])
    gap = assets - liabilities_equity
    if abs(gap) > 1e-6:
        raise ValueError(f"{year}: balance-sheet gap is {gap:.6f}")
    if p["cash"] < MIN_CASH - 1e-6:
        raise ValueError(f"{year}: cash is below minimum by {MIN_CASH - p['cash']:.6f}")


def project_year(opening, sga_ratio):
    """Calculate one year in the specified income, balance-sheet, and cash-flow order."""
    p = {}
    p["revenue"] = opening["revenue"] * (1 + REVENUE_GROWTH)
    p["gross_profit"] = p["revenue"] * GROSS_MARGIN
    p["sga"] = p["gross_profit"] * sga_ratio
    p["depreciation"] = opening["ppe"] * DEPR_RATIO
    p["impairment"] = IMPAIRMENT
    p["operating_income"] = p["gross_profit"] - p["sga"] - p["depreciation"] - p["impairment"]
    p["interest"] = (opening["floor_plan"] * FLOOR_PLAN_RATE
                     + opening["term_debt"] * TERM_DEBT_RATE
                     + opening["revolver"] * REVOLVER_RATE)
    p["pretax_income"] = p["operating_income"] - p["interest"]
    p["tax"] = max(0.0, p["pretax_income"]) * TAX_RATE
    p["net_income"] = p["pretax_income"] - p["tax"]

    p["inventory"] = (p["revenue"] - p["gross_profit"]) * INVENTORY_DAYS / 365
    p["floor_plan"] = p["inventory"] * FLOOR_PLAN_RATIO
    p["ppe"] = opening["ppe"] + CAPEX - p["depreciation"]
    p["change_in_other_working_capital"] = OWC_RATE * (p["revenue"] - opening["revenue"])
    p["other_assets"] = opening["other_assets"] + p["change_in_other_working_capital"] - p["impairment"]
    p["repayment"] = min(REPAYMENT, opening["term_debt"])
    p["term_debt"] = opening["term_debt"] - p["repayment"]
    p["other_liabilities"] = opening["other_liabilities"]
    p["buyback"] = BUYBACK
    p["equity"] = opening["equity"] + p["net_income"] - p["buyback"]

    p["change_in_inventory"] = p["inventory"] - opening["inventory"]
    p["change_in_floor_plan"] = p["floor_plan"] - opening["floor_plan"]
    p["capex"] = CAPEX
    p["fcfe"] = (p["net_income"] + p["depreciation"] + p["impairment"] - p["capex"]
                 - p["change_in_inventory"] - p["change_in_other_working_capital"]
                 + p["change_in_floor_plan"] - p["repayment"])
    cash_before_revolver = opening["cash"] + p["fcfe"] - p["buyback"]
    p["revolver"] = opening["revolver"]
    if cash_before_revolver < MIN_CASH:
        draw = min(MIN_CASH - cash_before_revolver, REVOLVER_LIMIT - p["revolver"])
        p["revolver"] += draw
        p["cash"] = cash_before_revolver + draw
    else:
        revolver_repayment = min(p["revolver"], cash_before_revolver - MIN_CASH)
        p["revolver"] -= revolver_repayment
        p["cash"] = cash_before_revolver - revolver_repayment
    return p


def print_table(title, rows, projections):
    print(f"\n{title} (USD millions)")
    print(f"{'':<32}" + "".join(f"{year:>12}" for year in YEARS))
    print("-" * 92)
    for label, key in rows:
        print(f"{label:<32}" + "".join(f"{p[key]:>12,.1f}" for p in projections))


def value_equity(projections):
    pv_fcfe = sum(p["fcfe"] / (1 + COST_OF_EQUITY) ** n
                  for n, p in enumerate(projections, 1))
    final = projections[-1]
    terminal_value = ((final["fcfe"] + final["repayment"]) * (1 + TERMINAL_GROWTH)
                      / (COST_OF_EQUITY - TERMINAL_GROWTH))
    pv_terminal = terminal_value / (1 + COST_OF_EQUITY) ** 5
    equity_value = pv_fcfe + pv_terminal
    return equity_value, pv_terminal / equity_value, equity_value / SHARES


def main():
    if TERMINAL_GROWTH >= COST_OF_EQUITY:
        raise ValueError("terminal growth must be below cost of equity")
    projections, opening = [], OPENING.copy()
    for year, sga_ratio in zip(YEARS, SGA_RATIOS):
        p = project_year(opening, sga_ratio)
        projections.append(p)
        opening = p

    print_table("Income Statement", [
        ("Revenue", "revenue"), ("Gross profit", "gross_profit"), ("SG&A", "sga"),
        ("Depreciation", "depreciation"), ("Impairment", "impairment"),
        ("Operating income", "operating_income"), ("Interest expense", "interest"),
        ("Pretax income", "pretax_income"), ("Tax expense", "tax"), ("Net income", "net_income"),
    ], projections)
    print_table("Balance Sheet", [
        ("Inventory", "inventory"), ("PP&E", "ppe"), ("Other assets", "other_assets"),
        ("Cash", "cash"), ("Floor plan", "floor_plan"), ("Term debt", "term_debt"),
        ("Revolver", "revolver"), ("Other liabilities", "other_liabilities"), ("Equity", "equity"),
    ], projections)
    print_table("Cash Flow / FCFE", [
        ("Net income", "net_income"), ("Depreciation", "depreciation"), ("Impairment", "impairment"),
        ("Capital spending", "capex"), ("Change in inventory", "change_in_inventory"),
        ("Change in other working capital", "change_in_other_working_capital"),
        ("Change in floor plan", "change_in_floor_plan"), ("Debt repayment", "repayment"),
        ("FCFE", "fcfe"), ("Share buyback", "buyback"),
    ], projections)

    print("\nAnnual Checks")
    for year, p in zip(YEARS, projections):
        assets = p["inventory"] + p["ppe"] + p["other_assets"] + p["cash"]
        liabilities_equity = p["floor_plan"] + p["term_debt"] + p["revolver"] + p["other_liabilities"] + p["equity"]
        print(f"{year}: assets - liabilities - equity = {assets - liabilities_equity:.1f}; "
              f"cash >= minimum: {p['cash'] >= MIN_CASH}")
        assert_balanced(year, p)

    equity_value, terminal_share, per_share = value_equity(projections)
    print(f"\nEquity value: {equity_value:,.2f}")
    print(f"Share of value after 2030: {terminal_share:.2%}")
    print(f"Value per share: {per_share:,.2f}")


if __name__ == "__main__":
    main()
