"""Single-peer AAPL/GRMN EV/EBITDA cross-check; USD millions unless noted."""

VALUATION_DATE = "September 9, 2026"
COMPANIES = {
    "AAPL": {"price": 315.34, "shares": 14776.353, "cash": 35934.0,
             "debt": 98657.0, "ebit": 133050.0, "da": 11698.0,
             "diluted_shares": 15004.697},
    "GRMN": {"price": 272.18, "shares": 192.480830, "cash": 2278.646,
             "debt": 0.0, "ebit": 1876.076, "da": 184.979,
             "diluted_shares": None},
}


def market_cap(company):
    return company["price"] * company["shares"]


def ebitda(company):
    return company["ebit"] + company["da"]


def enterprise_value(company):
    return market_cap(company) + company["debt"] - company["cash"]


def main():
    aapl, grmn = COMPANIES["AAPL"], COMPANIES["GRMN"]
    if any(value is None for value in grmn.values() if value is not grmn["diluted_shares"]):
        raise SystemExit("CONCLUSION: UNRESOLVED — required Garmin input missing.")
    if aapl["diluted_shares"] is None:
        raise SystemExit("CONCLUSION: UNRESOLVED — AAPL diluted-share input missing.")

    grmn_ev, grmn_ebitda = enterprise_value(grmn), ebitda(grmn)
    multiple = grmn_ev / grmn_ebitda
    implied_ev = multiple * ebitda(aapl)
    implied_equity = implied_ev - aapl["debt"] + aapl["cash"]
    implied_share = implied_equity / aapl["diluted_shares"]

    print("AAPL/GRMN single-peer EV/EBITDA cross-check")
    print(f"Valuation-date price convention: {VALUATION_DATE}")
    print("Formula/unit check: market cap = USD/share × million shares = USD millions.")
    print("EV = market cap + interest-bearing debt − cash and cash equivalents.")
    print("EBITDA = reported EBIT + reported depreciation and amortization.")
    print(f"GRMN market capitalization: ${market_cap(grmn):,.3f}M")
    print(f"GRMN EBITDA: ${grmn_ebitda:,.3f}M")
    print(f"GRMN enterprise value: ${grmn_ev:,.3f}M")
    print(f"GRMN EV/EBITDA: {multiple:.4f}x")
    print(f"AAPL implied enterprise value: ${implied_ev:,.3f}M")
    print(f"AAPL implied equity value: ${implied_equity:,.3f}M")
    print(f"AAPL implied value per diluted share: ${implied_share:.2f}")
    print("Conclusion: separate single-peer cross-check only; do not average with DCF or P/E.")


if __name__ == "__main__":
    main()
