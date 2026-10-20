"""Print Meridian's stated mandate and check supplied candidate allocations.

This module reports the existing mandate without selecting an optimizer,
security, allocation, or interpretation of the unresolved loss convention.
Allocation weights are expressed as percentage points (for example, 8.0).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


ISSUER_LIMIT_PERCENT = 8.0
RESERVE_REQUIREMENT_DOLLARS = 3_000_000.0
WEIGHT_TOLERANCE = 1e-6
CANDIDATE_E_WEIGHTS = {
    "Treasury bills": 0.0,
    "Treasury 10-year note": 0.0,
    "Investment-grade bond fund": 40.0,
    "Global equity index fund": 60.0,
}
RESERVE_ELIGIBLE_SLEEVES = {"Treasury bills", "Treasury 10-year note"}


def load_mandate(path: str | Path) -> dict:
    """Load the supplied Meridian mandate record."""
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


def check_candidate_allocation(
    weights: Mapping[str, float],
    *,
    issuer_weights: Mapping[str, float] | None = None,
    reserve_eligible_weights: Mapping[str, float] | None = None,
    portfolio_value: float | None = None,
) -> dict[str, object]:
    """Check stated mechanical constraints for a supplied candidate allocation.

    ``weights``, ``issuer_weights``, and ``reserve_eligible_weights`` use
    percentage points.  Issuer and reserve checks are reported as unavailable
    when their supporting data is not supplied.  This function does not rank,
    recommend, or create a candidate allocation.
    """
    total_weight = sum(weights.values())
    long_only_no_borrowing = all(weight >= -WEIGHT_TOLERANCE for weight in weights.values())

    if issuer_weights is None:
        issuer_limit = None
    else:
        issuer_limit = all(weight <= ISSUER_LIMIT_PERCENT + WEIGHT_TOLERANCE for weight in issuer_weights.values())

    if reserve_eligible_weights is None:
        reserve_eligible_weight = None
        reserve_requirement = None
    else:
        reserve_eligible_weight = sum(reserve_eligible_weights.values())
        reserve_requirement = (
            None
            if portfolio_value is None
            else reserve_eligible_weight / 100.0 * portfolio_value
            >= RESERVE_REQUIREMENT_DOLLARS - WEIGHT_TOLERANCE
        )

    return {
        "weights_sum_to_100_percent": abs(total_weight - 100.0) <= WEIGHT_TOLERANCE,
        "total_weight_percent": total_weight,
        "long_only_no_borrowing": long_only_no_borrowing,
        "no_issuer_above_8_percent": issuer_limit,
        "reserve_eligible_weight_percent": reserve_eligible_weight,
        "meets_3m_reserve_requirement": reserve_requirement,
    }


def is_unresolved(value: object) -> bool:
    """Return whether mandate wording explicitly leaves an item unresolved."""
    return "unresolved" in str(value).lower() or "requires clarification" in str(value).lower()


def print_mandate_check(mandate: Mapping[str, object]) -> None:
    """Print the mandate facts and the required escalation state."""
    print("MERIDIAN_MANDATE_CHECK")
    print("Objective:")
    print(f"- {mandate['objective']}")
    print("Hard constraints:")
    for constraint in mandate["constraints"]:
        print(f"- {constraint}")
    print("Unresolved CIO question:")
    print(f"- {mandate['unresolved_ambiguity']}")

    if is_unresolved(mandate["objective"]) or is_unresolved(mandate["risk_measure"]):
        print("DEFERRED_NO_ADOPTABLE_CANDIDATE")
        print(
            "No adoptable allocation can be recommended until the CIO clarifies "
            "the loss-limit convention and optimization tradeoff."
        )


def print_candidate_e_check() -> None:
    """Report Candidate E's reserve result without endorsing the candidate."""
    reserve_weights = {
        sleeve: CANDIDATE_E_WEIGHTS[sleeve]
        for sleeve in RESERVE_ELIGIBLE_SLEEVES
    }
    check = check_candidate_allocation(
        CANDIDATE_E_WEIGHTS,
        reserve_eligible_weights=reserve_weights,
    )

    print("CANDIDATE_E_CHECK")
    print("Weights:")
    for sleeve, weight in CANDIDATE_E_WEIGHTS.items():
        print(f"- {sleeve}: {weight:.1f}%")
    print(
        "Reserve-eligible weight: "
        f"{check['reserve_eligible_weight_percent']:.1f}%"
    )
    print("FAIL: Candidate E fails the Meridian reserve rule because its reserve-eligible weight is 0.0%.")
    print("Candidate E is not otherwise certified as mandate-compliant or adoptable; the Lab 13 ambiguity remains unresolved.")


if __name__ == "__main__":
    record = load_mandate(Path(__file__).with_name("mandate_template.json"))
    print_mandate_check(record)
    print()
    print_candidate_e_check()
