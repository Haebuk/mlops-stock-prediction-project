from datetime import datetime

import polars as pl
from polygon import RESTClient

from utils import load_polygon_api_key


def _agg_to_dict(data):
    # exclude otc
    return {
        "open": data.open,
        "high": data.high,
        "low": data.low,
        "close": data.close,
        "volume": data.volume,
        "vwap": data.vwap,
        "timestamp": datetime.fromtimestamp(data.timestamp / 1000),
        "transactions": data.transactions,
    }


def _aggs_to_dicts(aggs):
    return [_agg_to_dict(agg) for agg in aggs]


def get_aggregates(ticker, from_, to, multiplier=1, timespan="hour"):
    client = RESTClient(api_key=load_polygon_api_key())

    aggs = []
    for a in client.list_aggs(
        ticker=ticker,
        multiplier=multiplier,
        timespan=timespan,
        from_=from_,
        to=to,
        limit=50000,
    ):
        aggs.append(a)
    return aggs


def aggs_to_df(aggs, gte, lt):
    aggs = _aggs_to_dicts(aggs)
    df = pl.from_dicts(aggs)

    df = df.with_columns(pl.col("volume").cast(pl.Int64))

    gte = datetime.fromisoformat(gte)
    lt = datetime.fromisoformat(lt)

    df = df.filter((pl.col("timestamp") >= gte) & (pl.col("timestamp") < lt))
    return df
