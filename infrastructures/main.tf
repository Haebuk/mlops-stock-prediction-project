terraform {
  required_version = ">= 1.0"
  backend "gcs" {
    bucket = "tf-state-kade"
    prefix = "state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

module "bigquery" {
  source = "./modules/bigquery"
}
