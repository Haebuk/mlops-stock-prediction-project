import os
from polygon import RESTClient

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
client = RESTClient(api_key=POLYGON_API_KEY)

ticker = "SPY"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(
    ticker=ticker,
    multiplier=5,
    timespan="minute",
    from_="2023-07-01",
    to="2023-07-31",
    limit=50000,
):
    aggs.append(a)

print(aggs)

# # Get Last Trade
# trade = client.get_last_trade(ticker=ticker)
# print(trade)

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
