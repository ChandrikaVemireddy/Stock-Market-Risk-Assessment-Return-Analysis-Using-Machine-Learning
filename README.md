# AI-Based Stock Market Risk Assessment and Return Analysis Using Machine Learning

## Overview

This project develops a machine-learning framework for assessing stock-market risk and analysing returns using historical daily market data.

The study focuses on 10 selected Indian companies and uses NIFTY 50 as the market benchmark for Beta and comparative risk analysis.

## Study Period

**1 January 2019 to 31 December 2025**

- Training period: 2019–2023
- Testing period: 2024–2025

## Companies

| Company | NSE Symbol | Sector |
|---|---|---|
| State Bank of India | SBIN | Banking |
| Bharti Airtel Ltd. | BHARTIARTL | Telecommunications |
| Mahindra & Mahindra Ltd. | M&M | Automobile |
| Sun Pharmaceutical Industries Ltd. | SUNPHARMA | Healthcare |
| ITC Ltd. | ITC | FMCG |
| Larsen & Toubro Ltd. | LT | Construction |
| NTPC Ltd. | NTPC | Power |
| Tata Steel Ltd. | TATASTEEL | Metals |
| Maruti Suzuki India Ltd. | MARUTI | Automobile |
| Hindalco Industries Ltd. | HINDALCO | Metals |

## Data Source

Historical market data is intended to be collected directly from the **National Stock Exchange of India (NSE)**.

The raw dataset is expected to contain daily observations such as Date, Open, High, Low, Close, Volume/Shares Traded, and Turnover.

NIFTY 50 historical data is used as the market benchmark.

## Features

The project derives Daily Return, Annual Return, Annualized Volatility, Sharpe Ratio, Beta against NIFTY 50, Maximum Drawdown, Moving Averages, RSI, and volume-based features.

Risk observations are classified into Low Risk, Medium Risk, and High Risk.

## Machine Learning Models

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

## Evaluation

Models will be evaluated using Accuracy, Precision, Recall/Sensitivity, Specificity, F1 Score, and Confusion Matrix.

Feature importance will also be analysed for the tree-based models.

## Workflow

NSE Historical Data → Data Cleaning → Feature Engineering → Risk Classification → Time-Based Train/Test Split → Decision Tree / Random Forest / SVM → Evaluation → Risk and Return Analysis

## Repository Structure

```text
stock-market-risk-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── risk_classification.py
│   └── model_training.py
└── reports/
```

## Setup

```bash
pip install -r requirements.txt
```

## Current Status

This repository contains the initial project structure and documentation. The complete NSE data-collection and modelling pipeline will be implemented during the project.

No fabricated model results are included.

## Disclaimer

This is an academic/research project for studying historical market-risk patterns using machine learning. It is not financial advice or a recommendation to buy or sell securities.
