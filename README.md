# mlops-stock-prediction-project
Stock prediction Project for MLOps zoomcamp

## Target Stock
```json
{
    "results": [
        {
            "ticker": "SPY",
            "name": "SPDR S&P 500 ETF Trust",
            "market": "stocks",
            "locale": "us",
            "primary_exchange": "ARCX",
            "type": "ETF",
            "active": true,
            "currency_name": "usd",
            "cik": "0000884394",
            "composite_figi": "BBG000BDTBL9",
            "share_class_figi": "BBG001S72SM3",
            "last_updated_utc": "2023-07-14T00:00:00Z"
        }
    ],
    "status": "OK",
    "request_id": "c70fa9eba20d317b1cc731626fd32ba3",
    "count": 1
}
```
I used SPY ETF as a target stock. It is a ETF that tracks S&P 500 index. It is a good representative of US stock market.

## Pre-requisites
- Python 3.10
- Terraform
- I used [polygon.io](https://polygon.io/) API for stock data. You need to get api key from polygon.io and set it as an environment variable.

```bash
$ export POLYGON_API_KEY=<your api key>

or

$ vi polygon.api
<your api key>
```

1. 데이터를 api로 불러오고 데이터프레임화 한 후 parquet로 저장
2. 해당 데이터는 단발성 데이터이므로 한번에 불러와서 빅쿼리로 로드
3. 이후 매시 트리거 되는 파이프라인 개발
4. 기존 데이터로 학습
5. 매시 저장될 때 마다 학습하는 모델 개발
6. 모델 배포
7. 모니터링 환경 구축