"""AAPL comparable-company P/E case; inputs are intentionally editable below."""

from decimal import Decimal, ROUND_HALF_UP
from statistics import median


# Editable case inputs. Use None for an unavailable price or diluted EPS.
TARGET = {
    "ticker": "AAPL",
    "name": "Apple",
    "price": Decimal("315.34"),
    "diluted_eps": Decimal("7.46"),
}
PEERS = [
    {
        "ticker": "GRMN",
        "name": "Garmin",
        "price": Decimal("272.18"),
        "diluted_eps": Decimal("8.59"),
    },
    {
        "ticker": "LOGI",
        "name": "Logitech",
        "price": Decimal("98.69"),
        "diluted_eps": Decimal("4.80"),
    },
]


CENT = Decimal("0.01")


def money(value):
    """Format a Decimal as dollars rounded only for display."""
    return f"${value.quantize(CENT, rounding=ROUND_HALF_UP):,.2f}"


def signed_money(value):
    """Format a positive or negative Decimal as a dollar change."""
    sign = "+" if value >= 0 else "-"
    return f"{sign}{money(abs(value))}"


def valid_multiple(peer):
    """Return the unrounded P/E, or None when the input is not meaningful."""
    price = peer.get("price")
    eps = peer.get("diluted_eps")
    if price is None or eps is None or price <= 0 or eps <= 0:
        return None
    return price / eps


def unique_non_target_peers(peers, target_ticker):
    """Keep the first occurrence of each peer ticker and omit the target."""
    unique_peers = []
    seen = set()
    for peer in peers:
        ticker = peer.get("ticker", "").upper()
        if ticker == target_ticker.upper() or ticker in seen:
            continue
        seen.add(ticker)
        unique_peers.append(peer)
    return unique_peers


def median_multiple(valid_peers):
    return median([peer["pe"] for peer in valid_peers])


def main():
    target_eps = TARGET["diluted_eps"]
    if target_eps is None or target_eps <= 0:
        raise ValueError("Target diluted EPS must be positive for implied prices.")

    peers = unique_non_target_peers(PEERS, TARGET["ticker"])
    valid_peers = []

    print(f"Target: {TARGET['name']} ({TARGET['ticker']})")
    print(f"Target price: {money(TARGET['price'])}")
    print(f"Target diluted EPS: {target_eps:.2f}")
    print()
    print("Peer P/E multiples:")
    for peer in peers:
        pe = valid_multiple(peer)
        if pe is None:
            print(f"- {peer['name']} ({peer['ticker']}): not meaningful")
        else:
            peer_with_multiple = {**peer, "pe": pe}
            valid_peers.append(peer_with_multiple)
            print(f"- {peer['name']} ({peer['ticker']}): {pe:.6f}x")

    if not valid_peers:
        print("\nNo usable peers.")
        return

    multiples = [peer["pe"] for peer in valid_peers]
    low_pe = min(multiples)
    middle_pe = median_multiple(valid_peers)
    high_pe = max(multiples)

    print("\nPeer P/E summary:")
    if len(valid_peers) == 1:
        implied_price = middle_pe * target_eps
        print(f"- Reference estimate: {middle_pe:.6f}x; implied AAPL price {money(implied_price)}")
    else:
        print(f"- Minimum: {low_pe:.6f}x")
        print(f"- Median: {middle_pe:.6f}x")
        print(f"- Maximum: {high_pe:.6f}x")
        print(f"- Implied AAPL price range: {money(low_pe * target_eps)}–{money(high_pe * target_eps)}")
        print(f"- Median-implied AAPL price: {money(middle_pe * target_eps)}")

    full_median_price = middle_pe * target_eps
    print("\nPeer-removal check:")
    for removed_peer in valid_peers:
        remaining = [peer for peer in valid_peers if peer["ticker"] != removed_peer["ticker"]]
        if not remaining:
            print(f"- Remove {removed_peer['ticker']}: no usable peers remain")
            continue
        remaining_price = median_multiple(remaining) * target_eps
        change = remaining_price - full_median_price
        print(
            f"- Remove {removed_peer['ticker']}: remaining median-implied AAPL price "
            f"{money(remaining_price)}; change {signed_money(change)}"
        )


if __name__ == "__main__":
    main()
