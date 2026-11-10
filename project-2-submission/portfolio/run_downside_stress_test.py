"""Run the locked Project 2 downside stress test once."""

from itertools import product
from pathlib import Path

from portfolio import (
    build_covariance_matrix,
    estimate_annual_inputs_from_csv,
    expected_portfolio_return,
    portfolio_volatility,
    reserve_eligible_weight,
    validate_correlation_table,
)


OBJECTIVE_NET_RETURN = 0.065
IMPLEMENTATION_COST = 0.0025
RESERVE_MINIMUM = 0.03
STEP = 0.05
RESERVE_ELIGIBLE = {"SGOV", "VGIT"}
STRESSED_VTI_RETURN = -0.25
PRICES_PATH = Path(__file__).with_name("prices.csv")
STOP_MESSAGE = "No qualifying portfolio—do not allocate; escalate for CIO guidance."


def main() -> None:
    """Evaluate every locked-scenario grid candidate using copied portfolio math."""
    estimates = estimate_annual_inputs_from_csv(PRICES_PATH)
    assets = tuple(estimates["tickers"])
    expected_returns = dict(estimates["expected_returns"])
    expected_returns["VTI"] = STRESSED_VTI_RETURN
    volatilities = estimates["volatilities"]
    correlations = estimates["correlations"]

    validate_correlation_table(assets, correlations)
    covariance_matrix = build_covariance_matrix(assets, volatilities, correlations)
    increments = round(1.0 / STEP)
    best: dict[str, object] | None = None

    for partial_weights in product(range(increments + 1), repeat=len(assets) - 1):
        final_weight = increments - sum(partial_weights)
        if final_weight < 0:
            continue
        weights = {
            asset: integer_weight * STEP
            for asset, integer_weight in zip(assets, (*partial_weights, final_weight))
        }
        gross_return = expected_portfolio_return(weights, expected_returns)
        net_return = gross_return - IMPLEMENTATION_COST
        reserve_weight = reserve_eligible_weight(weights, RESERVE_ELIGIBLE)
        if net_return < OBJECTIVE_NET_RETURN or reserve_weight < RESERVE_MINIMUM:
            continue
        volatility = portfolio_volatility(weights, assets, covariance_matrix)
        if best is None or volatility < float(best["volatility"]):
            best = {
                "weights": weights,
                "gross_return": gross_return,
                "net_return": net_return,
                "volatility": volatility,
                "reserve_weight": reserve_weight,
            }

    print("DOWNSIDE_STRESS_TEST")
    print(f"Months used: {estimates['months_used']}")
    print(f"Effective stressed VTI return: {STRESSED_VTI_RETURN:.2%}")
    print(
        "Cost treatment: subtract 0.25 percentage points of annual "
        "implementation cost from each candidate's gross expected return."
    )
    print(
        "Candidate qualification rule: net expected return >= 6.50% and "
        "reserve-eligible weight >= 3.00%."
    )

    if best is None:
        print(STOP_MESSAGE)
        return

    print("Lowest-volatility qualifying mix")
    for asset in assets:
        print(f"{asset} weight: {best['weights'][asset]:.2%}")
    print(f"Gross expected return: {best['gross_return']:.2%}")
    print(f"Net expected return: {best['net_return']:.2%}")
    print(f"Volatility: {best['volatility']:.2%}")
    print(f"Reserve-eligible weight: {best['reserve_weight']:.2%}")


if __name__ == "__main__":
    main()
