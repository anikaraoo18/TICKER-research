"""Five-year FCFF discounted cash flow valuation (USD millions)."""

"""Five-year FCFF discounted cash flow valuation (USD millions)."""

# AAPL inputs - see AAPL_Lab_06_input_table.md for sources and estimate labels.
starting_fcff = 98767.0  # USD millions; FY2025 CFO-less-capex proxy (estimate)
growth_rates = [0.03, 0.0275, 0.025, 0.0225, 0.02]  # Years 1-5 estimates
wacc = 0.101429  # 10.1429% estimate
terminal_growth = 0.02  # 2.00% estimate
non_operating_cash = 35934.0  # USD millions; placeholder
debt = 98657.0  # USD millions
diluted_shares = 15004.697  # millions

# Sensitivity and reverse-DCF inputs.
sensitivity_wacc_values = [0.091429, 0.101429, 0.111429]
sensitivity_terminal_growth_values = [0.01, 0.02, 0.03]
target_share_price = 315.34  # USD per share; September 9, 2026 close
reverse_shift_lower_bound = -0.05  # -5 percentage points
reverse_shift_upper_bound = 0.10  # +10 percentage points


def calculate_valuation(projected_growth_rates, discount_rate, perpetuity_growth):
    """Return DCF outputs for the supplied growth, WACC, and terminal-growth inputs."""
    if perpetuity_growth >= discount_rate:
        raise ValueError("terminal growth must be less than WACC")

    projected_fcff = []
    prior_fcff = starting_fcff
    for growth_rate in projected_growth_rates:
        prior_fcff *= 1 + growth_rate
        projected_fcff.append(prior_fcff)

    explicit_pv = sum(
        cash_flow / (1 + discount_rate) ** year
        for year, cash_flow in enumerate(projected_fcff, start=1)
    )
    terminal_value = (
        projected_fcff[-1] * (1 + perpetuity_growth) / (discount_rate - perpetuity_growth)
    )
    terminal_pv = terminal_value / (1 + discount_rate) ** len(projected_fcff)
    enterprise = explicit_pv + terminal_pv
    equity = enterprise + non_operating_cash - debt

    return {
        "fcff": projected_fcff,
        "pv_explicit_fcff": explicit_pv,
        "terminal_value_year_5": terminal_value,
        "pv_terminal_value": terminal_pv,
        "enterprise_value": enterprise,
        "equity_value": equity,
        "value_per_diluted_share": equity / diluted_shares,
        "terminal_value_share_of_ev": terminal_pv / enterprise,
    }


def print_sensitivity_grid():
    """Print value per share for each WACC and terminal-growth combination."""
    print("\nSensitivity Grid: Value per Diluted Share")
    header = "WACC \\ Terminal Growth |" + "".join(
        f" {growth:>10.2%} |" for growth in sensitivity_terminal_growth_values
    )
    print(header)
    print("-" * len(header))

    for discount_rate in sensitivity_wacc_values:
        row = f"{discount_rate:>22.2%} |"
        for perpetuity_growth in sensitivity_terminal_growth_values:
            if perpetuity_growth >= discount_rate:
                cell = "invalid"
            else:
                value = calculate_valuation(
                    growth_rates, discount_rate, perpetuity_growth
                )["value_per_diluted_share"]
                cell = f"{value:.4f}"
            row += f" {cell:>10} |"
        print(row)


def reverse_dcf_shift():
    """Use bisection to find a uniform growth-rate shift matching the target price."""
    lower = reverse_shift_lower_bound
    upper = reverse_shift_upper_bound

    if lower > upper:
        return None, "No solution: lower bound is greater than upper bound."
    if any(rate + bound <= -1.0 for rate in growth_rates for bound in (lower, upper)):
        return None, (
            "No solution: this bracket pushes at least one annual growth rate to "
            "-100% or below."
        )

    def price_for_shift(shift):
        shifted_rates = [rate + shift for rate in growth_rates]
        return calculate_valuation(shifted_rates, wacc, terminal_growth)[
            "value_per_diluted_share"
        ]

    lower_difference = price_for_shift(lower) - target_share_price
    upper_difference = price_for_shift(upper) - target_share_price
    tolerance = 1e-10

    if abs(lower_difference) <= tolerance:
        return lower, None
    if abs(upper_difference) <= tolerance:
        return upper, None
    if lower_difference * upper_difference > 0:
        return None, "No solution in this bracket: target price is not reached."

    for _ in range(200):
        midpoint = (lower + upper) / 2
        midpoint_difference = price_for_shift(midpoint) - target_share_price
        if abs(midpoint_difference) <= tolerance:
            return midpoint, None
        if lower_difference * midpoint_difference < 0:
            upper = midpoint
            upper_difference = midpoint_difference
        else:
            lower = midpoint
            lower_difference = midpoint_difference

    return None, "No solution: bisection did not converge within 200 iterations."


def print_reverse_dcf():
    """Print the reverse-DCF result and every input held fixed."""
    solved_shift, message = reverse_dcf_shift()
    print("\nReverse DCF: Uniform Shift to All Five Explicit Growth Rates")
    print(f"Target Share Price: {target_share_price:.4f}")
    if message:
        print(message)
    else:
        print(f"Solved Uniform Growth-Rate Shift: {solved_shift:.8%}")
    print(
        "Inputs held fixed: "
        f"starting FCFF={starting_fcff:.4f}; "
        f"base growth rates={growth_rates}; "
        f"WACC={wacc:.4%}; terminal growth={terminal_growth:.4%}; "
        f"non-operating cash={non_operating_cash:.4f}; debt={debt:.4f}; "
        f"diluted shares={diluted_shares:.4f}."
    )


def main():
    if terminal_growth >= wacc:
        raise SystemExit(
            "Error: terminal growth must be less than WACC for the Gordon-growth model."
        )

    valuation = calculate_valuation(growth_rates, wacc, terminal_growth)
    fcff = valuation["fcff"]
    pv_explicit_fcff = valuation["pv_explicit_fcff"]
    terminal_value_year_5 = valuation["terminal_value_year_5"]
    pv_terminal_value = valuation["pv_terminal_value"]
    enterprise_value = valuation["enterprise_value"]
    equity_value = valuation["equity_value"]
    value_per_diluted_share = valuation["value_per_diluted_share"]
    terminal_value_share_of_ev = valuation["terminal_value_share_of_ev"]

    for year, cash_flow in enumerate(fcff, start=1):
        print(f"FCFF Year {year}: {cash_flow:.4f}")
    print(f"Present Value of Explicit FCFF: {pv_explicit_fcff:.4f}")
    print(f"Terminal Value at Year 5: {terminal_value_year_5:.4f}")
    print(f"Present Value of Terminal Value: {pv_terminal_value:.4f}")
    print(f"Enterprise Value: {enterprise_value:.4f}")
    print(f"Equity Value: {equity_value:.4f}")
    print(f"Value per Diluted Share: {value_per_diluted_share:.4f}")
    print(f"PV Terminal Value as Share of Enterprise Value: {terminal_value_share_of_ev:.4f}")
    print_sensitivity_grid()
    print_reverse_dcf()


if __name__ == "__main__":
    main()
