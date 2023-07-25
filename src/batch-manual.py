import os
import sys
import time

import polars as pl

from utils import get_from_to
from stocks import get_aggregates, aggs_to_df
from bigquery_utils import load_df_to_bigquery


def save_data(ticker, year, month, skip_if_exists=True):
    from_, to = get_from_to(year, month)

    if skip_if_exists:
        if os.path.exists(f"data/{year}_{month:02d}.parquet"):
            print(f"Skipping {year}_{month:02d}.parquet")
            return

    aggs = get_aggregates(ticker=ticker, from_=from_, to=to)

    df = aggs_to_df(aggs, gte=from_, lt=to)

    print(df)  # limit 5 requests in 1 minute

    os.makedirs("data", exist_ok=True)
    df.write_parquet(f"data/{year}_{month:02d}.parquet")

    time.sleep(12)
    return


def concat_data(ticker):
    df = pl.read_parquet("data/20*.parquet")
    print(df)

    df.write_parquet(f"data/{ticker}.parquet")

    return df


if __name__ == "__main__":
    ticker = "SPY"
    year = 2022
    for m in range(1, 13):
        save_data(ticker, year, month=m)

    year = 2023
    for m in range(1, 8):
        save_data(ticker, year, month=m)

    df = concat_data(ticker)

    load_df_to_bigquery(df.to_pandas(), is_overwrite=True)
