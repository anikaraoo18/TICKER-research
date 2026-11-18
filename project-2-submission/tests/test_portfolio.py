"""Known-answer and integrity tests for Project 2 portfolio calculations."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


PORTFOLIO_DIRECTORY = Path(__file__).resolve().parents[1] / "portfolio"
sys.path.insert(0, str(PORTFOLIO_DIRECTORY))

from portfolio import (  # noqa: E402
    CORRELATIONS,
    EXPECTED_RETURNS,
    RESERVE_ELIGIBLE_SLEEVES,
    SLEEVES,
    VOLATILITIES,
    benchmark_weights,
    build_covariance_matrix,
    equal_weight_weights,
    estimate_annual_inputs_from_csv,
    expected_portfolio_return,
    find_lowest_volatility_mix,
    portfolio_volatility,
    reserve_eligible_weight,
    validate_correlation_table,
)


PROJECT_DIRECTORY = Path(__file__).resolve().parents[1]
PRICES_PATH = PROJECT_DIRECTORY / "portfolio" / "prices.csv"


class PortfolioKnownAnswerTests(unittest.TestCase):
    """Check published Lab 14 answers and active-CSV integrity."""

    def test_lab14_benchmark_known_answer(self) -> None:
        covariance = build_covariance_matrix(SLEEVES, VOLATILITIES, CORRELATIONS)
        weights = benchmark_weights(SLEEVES)
        self.assertAlmostEqual(expected_portfolio_return(weights, EXPECTED_RETURNS), 0.068, places=12)
        self.assertAlmostEqual(portfolio_volatility(weights, SLEEVES, covariance), 0.1046, places=4)
        self.assertAlmostEqual(reserve_eligible_weight(weights, RESERVE_ELIGIBLE_SLEEVES), 0.0, places=12)

    def test_lab14_equal_weight_known_answer(self) -> None:
        covariance = build_covariance_matrix(SLEEVES, VOLATILITIES, CORRELATIONS)
        weights = equal_weight_weights(SLEEVES)
        self.assertAlmostEqual(expected_portfolio_return(weights, EXPECTED_RETURNS), 0.052, places=12)
        self.assertAlmostEqual(portfolio_volatility(weights, SLEEVES, covariance), 0.0521, places=4)
        self.assertAlmostEqual(reserve_eligible_weight(weights, RESERVE_ELIGIBLE_SLEEVES), 0.50, places=12)

    def test_active_csv_structure_and_60_month_mix(self) -> None:
        estimates = estimate_annual_inputs_from_csv(PRICES_PATH)
        self.assertEqual(estimates["tickers"], ("SGOV", "VGIT", "VCIT", "VTI"))
        self.assertEqual(estimates["months_used"], 60)
        mix = find_lowest_volatility_mix(
            estimates["tickers"],
            estimates["expected_returns"],
            estimates["volatilities"],
            estimates["correlations"],
            0.065,
            0.03,
            {"SGOV", "VGIT"},
        )
        self.assertIsNotNone(mix)
        assert mix is not None
        self.assertAlmostEqual(mix["weights"]["SGOV"], 0.65, places=12)
        self.assertAlmostEqual(mix["weights"]["VGIT"], 0.0, places=12)
        self.assertAlmostEqual(mix["weights"]["VCIT"], 0.0, places=12)
        self.assertAlmostEqual(mix["weights"]["VTI"], 0.35, places=12)
        self.assertAlmostEqual(mix["expected_return"], 0.0662, places=4)
        self.assertAlmostEqual(mix["volatility"], 0.0564, places=4)
        self.assertAlmostEqual(mix["reserve_eligible_weight"], 0.65, places=12)

    def test_rejects_invalid_correlation(self) -> None:
        broken = {asset: row.copy() for asset, row in CORRELATIONS.items()}
        broken["Treasury bills"]["Treasury 10-year note"] = 1.3
        with self.assertRaises(ValueError):
            validate_correlation_table(SLEEVES, broken)


if __name__ == "__main__":
    unittest.main()
