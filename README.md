# Stock Market Risk Assessment and Return Analysis Using Machine Learning

## 📌 Overview

This project presents an AI-based framework for assessing stock market risk and analyzing stock returns using historical financial data and machine learning techniques.

The study focuses on selected NSE-listed companies over the period from **1 January 2019 to 31 December 2025**. Historical market data is processed to calculate financial and technical indicators that represent stock returns, volatility, market sensitivity, and other risk characteristics.

Machine learning algorithms are then applied to classify stocks into different risk categories and compare their predictive performance.

The **NIFTY 50 Index** is used as the market benchmark for market-level analysis and Beta calculation.

---

## 🎯 Objectives

The major objectives of this project are:

- To collect historical stock market data for selected NSE-listed companies.
- To analyze stock returns and market risk using historical financial data.
- To calculate financial and technical indicators related to stock risk.
- To classify stocks into Low Risk, Medium Risk, and High Risk categories.
- To apply machine learning algorithms for stock risk classification.
- To compare the performance of different machine learning models.
- To identify the most important features contributing to stock risk classification.
- To analyze the relationship between stock risk and return.
- To compare the risk characteristics of companies from different sectors.

---

## 📊 Companies Selected for Analysis

The project considers the following ten NSE-listed companies:

| No. | Company | NSE Symbol | Sector |
|---|---|---|---|
| 1 | State Bank of India | SBIN | Banking |
| 2 | Bharti Airtel Ltd. | BHARTIARTL | Telecommunications |
| 3 | Mahindra & Mahindra Ltd. | M&M | Automobile |
| 4 | Sun Pharmaceutical Industries Ltd. | SUNPHARMA | Healthcare |
| 5 | ITC Ltd. | ITC | FMCG |
| 6 | Larsen & Toubro Ltd. | LT | Construction |
| 7 | NTPC Ltd. | NTPC | Power |
| 8 | Tata Steel Ltd. | TATASTEEL | Metals |
| 9 | Maruti Suzuki India Ltd. | MARUTI | Automobile |
| 10 | Hindalco Industries Ltd. | HINDALCO | Metals |

### Benchmark

The **NIFTY 50 Index** is used as the benchmark for market-related analysis, particularly for calculating Beta and comparing individual stock performance with the broader market.

---

## 📅 Study Period

The analysis covers historical market data from:

**1 January 2019 to 31 December 2025**

A time-based data split is used for machine learning:

- **Training Period:** 2019–2023
- **Testing Period:** 2024–2025

This approach helps evaluate the models on a later period rather than randomly mixing historical observations.

---

## 📈 Dataset

The project uses historical stock market information obtained from the **National Stock Exchange of India (NSE)**.

The raw market variables include:

- Date
- Open Price
- High Price
- Low Price
- Close Price
- Adjusted Close
- Trading Volume

The raw variables are processed and transformed into additional financial and technical features for risk and return analysis.

---

## ⚙️ Feature Engineering

Several financial and technical indicators are derived from the historical market data.

### Daily Return

Daily Return measures the percentage change in the stock price from one trading day to the next.

### Volatility

Volatility measures the variation in stock returns and is used as an important indicator of market risk.

### Sharpe Ratio

The Sharpe Ratio evaluates the return generated relative to the level of risk.

### Beta

Beta measures the sensitivity of an individual stock's returns relative to the **NIFTY 50 benchmark**.

### Maximum Drawdown

Maximum Drawdown measures the largest decline in stock value from a previous peak during the selected period.

### Moving Average

Moving averages are calculated to capture price trends and smooth short-term fluctuations.

### Relative Strength Index

The Relative Strength Index (RSI) is used as a technical indicator to measure the strength of recent price movements.

### Volume-Based Features

Trading volume and related indicators are used to capture changes in market participation and trading activity.

---

## 🏷️ Risk Classification

The project classifies stocks into three risk categories:

- **Low Risk**
- **Medium Risk**
- **High Risk**

The risk categories are derived from financial risk characteristics calculated from historical market data.

These categories are then used as the target variable for machine learning classification.

---

## 🤖 Machine Learning Models

Three machine learning algorithms are considered for stock risk classification.

### 1. Decision Tree

The Decision Tree algorithm is used to classify stocks into different risk categories using decision-based rules.

It also provides an interpretable representation of how different financial features contribute to the classification.

### 2. Random Forest

Random Forest combines multiple decision trees to improve classification performance and robustness.

It also provides feature importance values that can be used to identify the financial indicators that have greater influence on risk classification.

### 3. Support Vector Machine

Support Vector Machine (SVM) is used to identify decision boundaries between different risk categories.

It is evaluated along with Decision Tree and Random Forest to compare different machine learning approaches.

---

## 🧪 Training and Testing Methodology

A time-based train-test split is used in this project.

### Training Data

**2019–2023**

The training data is used to develop and train the machine learning models.

### Testing Data

**2024–2025**

The testing data is used to evaluate how well the trained models classify risk categories on later market observations.

This approach is more suitable for historical financial data because it maintains the chronological order of observations.

---

## 📏 Model Evaluation

The machine learning models are evaluated using multiple classification metrics:

- Accuracy
- Precision
- Recall / Sensitivity
- Specificity
- F1 Score
- Confusion Matrix

These metrics are used to compare the performance of Decision Tree, Random Forest, and Support Vector Machine models.

---

## 🔍 Feature Importance Analysis

Feature importance analysis is performed to determine which financial and technical indicators contribute most to stock risk classification.

This helps provide better insight into the relationship between market characteristics and stock risk.

Features such as volatility, return, Beta, Maximum Drawdown, Sharpe Ratio, moving averages, RSI, and volume-related measures can be analyzed for their contribution to the classification process.

---

## 📊 Stock Return Analysis

In addition to risk classification, the project analyzes stock return characteristics.

The return analysis includes:

- Daily returns
- Average returns
- Return variability
- Risk-adjusted performance
- Market sensitivity
- Drawdown characteristics

The objective is to understand how different stocks behave in terms of both **risk and return** over the study period.

---

## 🔄 Project Workflow

```text
Historical NSE Market Data
            ↓
       Data Collection
            ↓
       Data Preprocessing
            ↓
      Feature Engineering
            ↓
 Return and Risk Calculation
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
   Feature Importance
            ↓
 Stock Risk & Return Analysis
```

---

## 🗂️ Project Structure

```text
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
```

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Requests**
- **Jupyter Notebook**

---

---

## ▶️ Usage

The project modules can be executed as part of the complete workflow.

### Data Collection

```bash
python src/data_collection.py
```

### Data Preprocessing

```bash
python src/preprocessing.py
```

### Feature Engineering

```bash
python src/feature_engineering.py
```

### Risk Classification

```bash
python src/risk_classification.py
```

### Model Training

```bash
python src/model_training.py
```

The complete analysis can also be executed through Jupyter Notebook.

---

## 📌 Project Status

The repository currently contains the initial project structure and implementation modules.

The complete implementation will cover:

- NSE historical data collection
- Data preprocessing
- Feature engineering
- Financial risk calculation
- Return analysis
- Risk category generation
- Machine learning model training
- Model evaluation
- Feature importance analysis
- Comparison of machine learning models

Final model performance results and analytical findings will be added after completing the implementation and evaluation using the final dataset.

---

## 🌐 Data Source

Historical market data used in the project is based on information from the **National Stock Exchange of India (NSE)**.

The NIFTY 50 Index is used as the benchmark for market-level analysis.

---

