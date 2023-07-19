import time
import os

from utils import get_aggregates, aggs_to_df, get_from_to


def main(ticker, year, month):
    from_, to = get_from_to(year, month)

    aggs = get_aggregates(
        ticker=ticker,
        from_=from_,
        to=to,
    )

    df = aggs_to_df(aggs, gte=from_, lt=to)

    print(df)

    os.makedirs("data", exist_ok=True)
    df.write_parquet(f"data/{year}_{month:02d}.parquet")
    return


if __name__ == "__main__":
    ticker = "SPY"
    year = 2022

    for m in range(1, 13):
        main(ticker, year, month=m)
        time.sleep(12)  # limit 5 requests in 1 minute

    year = 2023
    for m in range(1, 8):
        main(ticker=ticker, year=year, month=m)
