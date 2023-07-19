import os
from datetime import datetime

import polars as pl
from polygon import RESTClient


def _load_polygon_api_key():
    """read polygon.io api key
    first check if polygon.api file in local directory exists
    if not, check if environment variable exists
    also if not, raise error
    """
    api_file_path = "polygon.api"
    if os.path.exists(api_file_path):
        with open(api_file_path, "r") as f:
            api_key = f.read()
    elif "POLYGON_API_KEY" in os.environ:
        api_key = os.environ["POLYGON_API_KEY"]
    else:
        raise ValueError("No polygon.io API key found")
    return api_key


def get_aggregates(ticker, from_, to, multiplier=1, timespan="hour"):
    client = RESTClient(api_key=_load_polygon_api_key())

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


def aggs_to_df(aggs, gte, lt):
    aggs = _aggs_to_dicts(aggs)
    df = pl.from_dicts(aggs)

    df = df.with_columns(pl.col("volume").cast(pl.Int64))

    gte = datetime.fromisoformat(gte)
    lt = datetime.fromisoformat(lt)

    df = df.filter((pl.col("timestamp") >= gte) & (pl.col("timestamp") < lt))
    return df


def get_from_to(year: int, month: int):
    if isinstance(year, str):
        year = int(year)
    if isinstance(month, str):
        month = int(month)

    from_ = f"{year}-{month:02d}-01"

    if month == 12:
        to = f"{year+1:04d}-01-01"
    else:
        to = f"{year}-{month+1:02d}-01"

    return from_, to
