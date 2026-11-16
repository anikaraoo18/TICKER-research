"""Compare the all-60-month portfolio search at two objective values."""

from pathlib import Path

from portfolio import estimate_annual_inputs_from_csv, find_lowest_volatility_mix


BASELINE_OBJECTIVE = 0.065
CHANGED_OBJECTIVE = 0.070
RESERVE_MINIMUM = 0.03
RESERVE_ELIGIBLE = {"SGOV", "VGIT"}
STEP = 0.05
EXPECTED_TICKERS = ("SGOV", "VGIT", "VCIT", "VTI")
PRICES_PATH = Path(__file__).with_name("prices.csv")


def search(objective: float, estimates: dict[str, object]) -> dict[str, object] | None:
    """Reuse the copied portfolio search with only the objective changed."""
    return find_lowest_volatility_mix(
        estimates["tickers"],
        estimates["expected_returns"],
        estimates["volatilities"],
        estimates["correlations"],
        objective,
        RESERVE_MINIMUM,
        RESERVE_ELIGIBLE,
        STEP,
    )


def largest_allocation_change(
    baseline: dict[str, object], changed: dict[str, object], assets: tuple[str, ...]
) -> float:
    """Return the greatest absolute sleeve-weight change between the two runs."""
    baseline_weights = baseline["weights"]
    changed_weights = changed["weights"]
    return max(abs(changed_weights[asset] - baseline_weights[asset]) for asset in assets)


def print_result(label: str, objective: float, result: dict[str, object], change: float) -> None:
    """Print one search result using stable percentage formatting."""
    print(label)
    print(f"Objective: {objective:.2%}")
    for asset in EXPECTED_TICKERS:
        print(f"{asset} weight: {result['weights'][asset]:.2%}")
    print(f"Expected return: {result['expected_return']:.2%}")
    print(f"Volatility: {result['volatility']:.2%}")
    print(f"Reserve-eligible weight: {result['reserve_eligible_weight']:.2%}")
    print(f"Largest allocation change from baseline: {change:.2%}")


def main() -> None:
    """Run the same 60-month search at the baseline and changed objectives."""
    estimates = estimate_annual_inputs_from_csv(PRICES_PATH)
    assets = estimates["tickers"]
    if assets != EXPECTED_TICKERS or estimates["months_used"] != 60:
        raise ValueError("Expected the 60-month SGOV/VGIT/VCIT/VTI price data.")

    baseline = search(BASELINE_OBJECTIVE, estimates)
    changed = search(CHANGED_OBJECTIVE, estimates)
    if baseline is None or changed is None:
        raise RuntimeError("Both objective tests must return a qualifying portfolio.")

    change = largest_allocation_change(baseline, changed, assets)
    print("LAB_20_OBJECTIVE_TEST")
    print(f"Months used: {estimates['months_used']}")
    print("Convention: compare the model's established expected-return field directly to the objective; no separate cost assumption is added or changed.")
    print_result("BASELINE", BASELINE_OBJECTIVE, baseline, 0.0)
    print_result("CHANGED_OBJECTIVE", CHANGED_OBJECTIVE, changed, change)
    print(f"Largest allocation change overall: {change:.2%}")
    print("Committee decision: Do not allocate or rebalance yet.")


if __name__ == "__main__":
    main()
