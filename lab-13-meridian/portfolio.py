"""Compare simple Meridian portfolio illustrations from editable annual inputs."""

from __future__ import annotations

from math import sqrt
from typing import Mapping, Sequence


# Editable annual inputs. Percentages are written as decimals (3.5% = 0.035).
SLEEVES = (
    "Treasury bills",
    "Treasury 10-year note",
    "Investment-grade bond fund",
    "Global equity index fund",
)
EXPECTED_RETURNS = {
    "Treasury bills": 0.035,
    "Treasury 10-year note": 0.043,
    "Investment-grade bond fund": 0.050,
    "Global equity index fund": 0.080,
}
VOLATILITIES = {
    "Treasury bills": 0.005,
    "Treasury 10-year note": 0.070,
    "Investment-grade bond fund": 0.060,
    "Global equity index fund": 0.160,
}
CORRELATIONS = {
    "Treasury bills": {
        "Treasury bills": 1.00,
        "Treasury 10-year note": 0.10,
        "Investment-grade bond fund": 0.05,
        "Global equity index fund": 0.00,
    },
    "Treasury 10-year note": {
        "Treasury bills": 0.10,
        "Treasury 10-year note": 1.00,
        "Investment-grade bond fund": 0.80,
        "Global equity index fund": -0.10,
    },
    "Investment-grade bond fund": {
        "Treasury bills": 0.05,
        "Treasury 10-year note": 0.80,
        "Investment-grade bond fund": 1.00,
        "Global equity index fund": 0.25,
    },
    "Global equity index fund": {
        "Treasury bills": 0.00,
        "Treasury 10-year note": -0.10,
        "Investment-grade bond fund": 0.25,
        "Global equity index fund": 1.00,
    },
}
OBJECTIVE_RETURN = 0.065
RESERVE_ELIGIBLE_SLEEVES = {"Treasury bills", "Treasury 10-year note"}
TOLERANCE = 1e-12


def validate_correlation_table(
    sleeves: Sequence[str], correlations: Mapping[str, Mapping[str, float]]
) -> None:
    """Raise ValueError unless the correlation table is valid and symmetric."""
    for left in sleeves:
        if left not in correlations:
            raise ValueError(f"Correlation table is missing row: {left}")
        for right in sleeves:
            if right not in correlations[left]:
                raise ValueError(f"Correlation table is missing {left}/{right}")
            value = correlations[left][right]
            if not -1.0 <= value <= 1.0:
                raise ValueError(
                    f"Correlation for {left}/{right} is {value}; it must be between -1 and 1."
                )
            if left == right and abs(value - 1.0) > TOLERANCE:
                raise ValueError(f"Diagonal correlation for {left} is {value}; it must be 1.")
            reverse_value = correlations.get(right, {}).get(left)
            if reverse_value is None or abs(value - reverse_value) > TOLERANCE:
                raise ValueError(f"Correlation table is not symmetric at {left}/{right}.")


def covariance_value(correlation: float, left_volatility: float, right_volatility: float) -> float:
    """Return covariance as correlation times the two volatilities."""
    return correlation * left_volatility * right_volatility


def build_covariance_matrix(
    sleeves: Sequence[str],
    volatilities: Mapping[str, float],
    correlations: Mapping[str, Mapping[str, float]],
) -> list[list[float]]:
    """Build a covariance matrix from correlations and annual volatilities."""
    return [
        [covariance_value(correlations[left][right], volatilities[left], volatilities[right])
         for right in sleeves]
        for left in sleeves
    ]


def benchmark_weights(sleeves: Sequence[str]) -> dict[str, float]:
    """Return the stated 60% equity / 40% investment-grade bond benchmark."""
    return {
        sleeve: 0.60 if sleeve == "Global equity index fund"
        else 0.40 if sleeve == "Investment-grade bond fund"
        else 0.0
        for sleeve in sleeves
    }


def equal_weight_weights(sleeves: Sequence[str]) -> dict[str, float]:
    """Allocate equally across all sleeves."""
    return {sleeve: 1.0 / len(sleeves) for sleeve in sleeves}


def inverse_volatility_weights(
    sleeves: Sequence[str], volatilities: Mapping[str, float]
) -> dict[str, float]:
    """Allocate in inverse proportion to volatility, scaled to 100%."""
    inverse_volatilities = {sleeve: 1.0 / volatilities[sleeve] for sleeve in sleeves}
    total_inverse_volatility = sum(inverse_volatilities.values())
    return {
        sleeve: inverse_volatilities[sleeve] / total_inverse_volatility
        for sleeve in sleeves
    }


def expected_portfolio_return(
    weights: Mapping[str, float], expected_returns: Mapping[str, float]
) -> float:
    """Calculate a portfolio's weighted expected return."""
    return sum(weights[sleeve] * expected_returns[sleeve] for sleeve in weights)


def portfolio_variance(
    weights: Mapping[str, float], sleeves: Sequence[str], covariance_matrix: Sequence[Sequence[float]]
) -> float:
    """Calculate w' covariance w."""
    return sum(
        weights[left] * covariance_matrix[row][column] * weights[right]
        for row, left in enumerate(sleeves)
        for column, right in enumerate(sleeves)
    )


def portfolio_volatility(
    weights: Mapping[str, float], sleeves: Sequence[str], covariance_matrix: Sequence[Sequence[float]]
) -> float:
    """Calculate portfolio volatility from portfolio variance."""
    return sqrt(max(portfolio_variance(weights, sleeves, covariance_matrix), 0.0))


def reserve_eligible_weight(weights: Mapping[str, float], eligible_sleeves: set[str]) -> float:
    """Calculate the weight in the stated reserve-eligible sleeves."""
    return sum(weights[sleeve] for sleeve in eligible_sleeves)


def meets_objective(expected_return: float, objective_return: float) -> bool:
    """Return whether expected return meets the stated objective return."""
    return expected_return >= objective_return


def print_portfolio(
    name: str,
    weights: Mapping[str, float],
    covariance_matrix: Sequence[Sequence[float]],
) -> None:
    """Calculate and print one portfolio's inputs-derived results."""
    expected_return = expected_portfolio_return(weights, EXPECTED_RETURNS)
    volatility = portfolio_volatility(weights, SLEEVES, covariance_matrix)
    reserve_weight = reserve_eligible_weight(weights, RESERVE_ELIGIBLE_SLEEVES)
    formatted_weights = ", ".join(
        f"{sleeve}: {weights[sleeve]:.1%}" for sleeve in SLEEVES
    )

    print(name)
    print(f"  Weights: {formatted_weights}")
    print(f"  Expected return: {expected_return:.2%}")
    print(f"  Volatility: {volatility:.2%}")
    print(f"  Reserve-eligible weight: {reserve_weight:.1%}")
    print(f"  Meets {OBJECTIVE_RETURN:.1%} objective: {'Yes' if meets_objective(expected_return, OBJECTIVE_RETURN) else 'No'}")


def main() -> None:
    """Validate inputs, build covariance, and report the three portfolios."""
    try:
        validate_correlation_table(SLEEVES, CORRELATIONS)
    except ValueError as error:
        print(f"INPUT ERROR: Refusing to run. {error}")
        return

    covariance_matrix = build_covariance_matrix(SLEEVES, VOLATILITIES, CORRELATIONS)
    portfolios = (
        ("Benchmark (40% investment-grade bonds / 60% global equities)", benchmark_weights(SLEEVES)),
        ("Equal weight", equal_weight_weights(SLEEVES)),
        ("Inverse volatility", inverse_volatility_weights(SLEEVES, VOLATILITIES)),
    )
    for index, (name, weights) in enumerate(portfolios):
        if index:
            print()
        print_portfolio(name, weights, covariance_matrix)


if __name__ == "__main__":
    main()
