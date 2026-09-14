#  Stock Market Risk Assessment and Return Analysis Using Machine Learning

## 📌 Overview

This project presents an AI-based framework for assessing stock market risk and analyzing stock returns using historical financial data and machine learning techniques.

The study focuses on selected NSE-listed companies over the period from **1 January 2019 to 31 December 2025**. Financial indicators and technical features are derived from historical market data and used to classify stocks into different risk categories.

Machine learning models are then trained and evaluated to determine their effectiveness in stock market risk classification.

The project also uses the **NIFTY 50 Index as a benchmark** for market-related analysis, including Beta calculation.

---

## 🎯 Objectives

The main objectives of this project are:

- To collect historical stock market data for selected NSE-listed companies.
- To analyze stock returns and market risk using financial indicators.
- To calculate important risk and technical indicators from historical price data.
- To classify stocks into **Low Risk, Medium Risk, and High Risk** categories.
- To apply machine learning algorithms for risk classification.
- To compare the performance of different machine learning models.
- To identify the features that contribute most to stock risk classification.
- To analyze stock returns and risk characteristics across different companies and sectors.

---

## 📊 Dataset

The study uses historical market data for the period:

**1 January 2019 – 31 December 2025**

The project focuses on the following NSE-listed companies:

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

### Benchmark

**NIFTY 50 Index**

The NIFTY 50 is used as the benchmark for market-level comparison and Beta analysis.

---

## 📈 Raw Market Variables

The historical market data contains variables such as:

- Date
- Open Price
- High Price
- Low Price
- Close Price
- Adjusted Close
- Trading Volume

These variables form the basis for calculating additional financial and technical features.

---

## ⚙️ Feature Engineering

The following features are considered for stock risk and return analysis:

### Return

Daily stock return is calculated from historical closing prices to measure the percentage change in stock value.

### Volatility

Volatility is used to measure the variation in stock returns and represents an important indicator of market risk.

### Sharpe Ratio

The Sharpe Ratio is used to evaluate return relative to the level of risk.

### Beta

Beta measures the sensitivity of a stock's movement relative to the **NIFTY 50 benchmark**.

### Maximum Drawdown

Maximum Drawdown measures the largest decline in stock value from a previous peak.

### Moving Average

Moving averages are used to identify trends in stock prices.

### RSI

The Relative Strength Index (RSI) is used as a technical indicator to measure the strength of recent price movements.

### Volume-Based Features

Trading volume is analyzed to capture changes in market participation and trading activity.

---

## 🏷️ Risk Classification

The project classifies stocks into three risk categories:

- **Low Risk**
- **Medium Risk**
- **High Risk**

These categories are used as the target variable for machine learning classification.

The classification is based on financial risk characteristics derived from historical market data.

---

## 🤖 Machine Learning Models

The project evaluates multiple machine learning algorithms for stock risk classification.

### 1. Decision Tree

A Decision Tree is used to create interpretable decision rules for classifying stocks into different risk categories.

### 2. Random Forest

Random Forest combines multiple decision trees to improve classification performance and provide feature importance information.

### 3. Support Vector Machine

Support Vector Machine (SVM) is used to identify boundaries between different stock risk categories.

---

## 🧪 Training and Testing

A time-based split is used to avoid using future information for training.

### Training Data

**2019 – 2023**

### Testing Data

**2024 – 2025**

This approach allows the models to be evaluated on a later time period and provides a more realistic assessment of their classification performance.

---

## 📏 Model Evaluation

The machine learning models are evaluated using:

- Accuracy
- Precision
- Recall / Sensitivity
- Specificity
- F1 Score
- Confusion Matrix

The performance of the models is compared to determine which algorithm provides better stock risk classification.

---

## 🔍 Feature Importance

Feature importance is analyzed to identify which financial and technical indicators contribute most to the prediction of stock risk.

This helps in understanding the relationship between market characteristics and risk classification.

---

## 🔄 Project Workflow

```text
Historical NSE Market Data
            ↓
       Data Collection
            ↓
       Data Cleaning
            ↓
    Feature Engineering
            ↓
 Return & Risk Calculation
            ↓
     Risk Classification
            ↓
     Train/Test Split
            ↓
 ┌──────────┬──────────┬──────────┐
 │ Decision │  Random  │   SVM    │
 │   Tree   │  Forest  │          │
 └──────────┴──────────┴──────────┘
            ↓
    Model Evaluation
            ↓
Feature Importance Analysis
            ↓
 Stock Risk & Return Analysis

📁 Project Structure
stock-market-risk-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│
└── src/
    ├── data_collection.py
    ├── preprocessing.py
    ├── feature_engineering.py
    ├── risk_classification.py
    └── model_training.py
🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Requests
- Jupyter Notebook
 Feature Importance Analysis
            ↓
 Stock Risk & Return Analysis
