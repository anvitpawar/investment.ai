from typing import List, Dict


class MockZerodhaClient:
    """A mock client that mimics Zerodha Kite responses for holdings and LTP.

    This client should never call live APIs. It's used for local dev and tests.
    """

    def authenticate(self) -> bool:
        return True

    async def fetch_holdings(self) -> List[Dict]:
        # Return sample holdings structure
        return [
            {"symbol": "RELIANCE", "instrument_type": "EQ", "quantity": 10, "average_price": 2200.0},
            {"symbol": "INFY", "instrument_type": "EQ", "quantity": 5, "average_price": 1500.0},
        ]

    async def fetch_mf_holdings(self) -> List[Dict]:
        return [
            {"symbol": "AXIS_BLUECHIP", "instrument_type": "MF", "quantity": 100, "average_price": 100.0},
        ]

    async def fetch_ltp(self, symbols: List[str]) -> Dict[str, float]:
        # Return mock last traded prices
        prices = {"RELIANCE": 2500.0, "INFY": 1600.0, "AXIS_BLUECHIP": 120.0}
        return {s: prices.get(s, 0.0) for s in symbols}
