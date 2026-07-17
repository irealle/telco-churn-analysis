# telco-churn-analysis

Exploratory data analysis and churn prediction on the IBM Telco Customer Churn dataset. Portfolio Project #1 — applying pandas/scikit-learn skills from ADM 3308.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run from the repo root so the relative data path resolves:

```bash
python src/telco_churn.py
```

## Data

`data/WA_Fn-UseC_-Telco-Customer-Churn.csv` — the IBM Telco Customer Churn dataset (despite the original `.xls` name, it's plain CSV). One row per customer; target column is `Churn`.

