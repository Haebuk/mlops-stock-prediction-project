from polygon import RESTClient

from src.utils import load_polygon_api_key


def test_load_api_key():
    api_key = load_polygon_api_key()
    assert isinstance(api_key, str)


def test_polygon_api_works():
    POLYGON_API_KEY = load_polygon_api_key()
    client = RESTClient(api_key=POLYGON_API_KEY)

    ticker = "SPY"

    # Get Last Trade
    aggs = []
    for a in client.list_aggs(
        ticker=ticker,
        multiplier=5,
        timespan="minute",
        from_="2023-07-01",
        to="2023-07-05",
        limit=50000,
    ):
        aggs.append(a)

    assert len(aggs) > 0


# List Aggregates (Bars)
#

# print(aggs)


# # List Trades
# trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
# for trade in trades:
#     print(trade)

# # Get Last Quote
# quote = client.get_last_quote(ticker=ticker)
# print(quote)

# # List Quotes
# quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
# for quote in quotes:
#     print(quote)
