from typing import List, Dict


def normalize_holdings(raw: List[Dict]) -> List[Dict]:
    """Convert broker-specific holdings into normalized position dicts."""
    normalized = []
    for r in raw:
        normalized.append(
            {
                "symbol": r.get("symbol"),
                "asset_class": "equity" if r.get("instrument_type") == "EQ" else "mf",
                "quantity": float(r.get("quantity", 0)),
                "average_price": float(r.get("average_price", 0.0)),
            }
        )
    return normalized
