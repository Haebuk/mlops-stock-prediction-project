###
# Copyright 2013-2023 AFI, Inc. All Rights Reserved.
###

import os

import pandas as pd
from google.cloud import bigquery

from constants import TABLE_ID, GOOGLE_APPLICATION_CREDENTIALS_PATH
from schema import BIGQUERY_SCHEMA

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS_PATH


def load_df_to_bigquery(df: pd.DataFrame, is_overwrite: bool = False):
    client = bigquery.Client()

    WRITE_DISPOSITION = "WRITE_TRUNCATE" if is_overwrite else "WRITE_APPEND"

    job_config = bigquery.LoadJobConfig(
        schema=BIGQUERY_SCHEMA,
        write_disposition=WRITE_DISPOSITION,
    )

    job = client.load_table_from_dataframe(df, TABLE_ID, job_config=job_config)
    job.result()

    table = client.get_table(TABLE_ID)
    print(f"Loaded {table.num_rows} rows to {TABLE_ID}.")
