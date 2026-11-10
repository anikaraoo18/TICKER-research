"""Run the locked Project 2 lookback-window changed-input test once."""

from pathlib import Path

from portfolio import estimate_annual_inputs_from_csv, find_lowest_volatility_mix


OBJECTIVE_RETURN = 0.065
RESERVE_MINIMUM = 0.03
RESERVE_ELIGIBLE = {"SGOV", "VGIT"}
PRICES_PATH = Path(__file__).with_name("prices.csv")


def run_case(label: str, *, last_36_months: bool) -> dict[str, object]:
    """Estimate CSV inputs and run the shared long-only grid search."""
    estimates = estimate_annual_inputs_from_csv(
        PRICES_PATH, last_36_months=last_36_months
    )
    assets = tuple(estimates["tickers"])
    result = find_lowest_volatility_mix(
        assets,
        estimates["expected_returns"],
        estimates["volatilities"],
        estimates["correlations"],
        OBJECTIVE_RETURN,
        RESERVE_MINIMUM,
        RESERVE_ELIGIBLE,
    )
    if result is None:
        raise RuntimeError(f"{label}: no qualifying mix.")

    print(label)
    print(f"Months used: {estimates['months_used']}")
    for asset in assets:
        print(f"{asset} weight: {result['weights'][asset]:.2%}")
    print(f"Expected return: {result['expected_return']:.2%}")
    print(f"Volatility: {result['volatility']:.2%}")
    print(f"Reserve-eligible weight: {result['reserve_eligible_weight']:.2%}")
    return result


def main() -> None:
    """Run only the locked all-history versus recent-history comparison."""
    baseline = run_case("Baseline: all 60 monthly observations", last_36_months=False)
    changed = run_case(
        "Changed input: most recent 36 monthly observations",
        last_36_months=True,
    )
    largest_change = max(
        abs(baseline["weights"][asset] - changed["weights"][asset])
        for asset in baseline["weights"]
    )
    print(f"Largest allocation change: {largest_change:.2%}")


if __name__ == "__main__":
    main()
