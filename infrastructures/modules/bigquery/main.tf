resource "google_bigquery_dataset" "stock_data" {
  dataset_id  = "stock_data"
  description = "dataset for stock data"
  location    = var.region
}

resource "google_bigquery_table" "spy" {
  dataset_id = google_bigquery_dataset.stock_data.dataset_id
  table_id   = "spy"

  time_partitioning {
    type  = "DAY"
    field = "timestamp"
  }

  schema = <<EOF
[
    {"name": "open", "type": "FLOAT"},
    {"name": "high", "type": "FLOAT"},
    {"name": "low", "type": "FLOAT"},
    {"name": "close", "type": "FLOAT"},
    {"name": "volume", "type": "INTEGER"},
    {"name": "vwap", "type": "FLOAT"},
    {"name": "timestamp", "type": "TIMESTAMP"},
    {"name": "transactions", "type": "INTEGER"}
]
EOF
}
