# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A small portfolio data-analysis project: exploratory analysis and (eventually) churn prediction on the IBM Telco Customer Churn dataset. Early stage — currently a single script doing basic data cleaning.

## Commands

```bash
# setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run (must be run from repo root — script uses a relative path to the data file)
python src/telco_churn.py
```

There is no test suite, linter, or build step configured yet.

## Structure

- `src/telco_churn.py` — analysis script, reads `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` via a path relative to the repo root
- `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` — the raw dataset. Despite the original filename's `.xls` extension, the file is plain CSV (`pd.read_csv`, not `pd.read_excel`)
- `requirements.txt` — `pandas`, `scikit-learn`

## Data notes

One row per customer; target column is `Churn`. `TotalCharges` arrives as a string with some blank values — cast with `pd.to_numeric(..., errors='coerce')` and fill NaNs before treating it as numeric (already handled in `telco_churn.py`).
