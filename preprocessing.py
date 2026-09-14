import pandas as pd

def clean_market_data(df):
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.sort_values('Date')
    df = df.drop_duplicates(subset='Date')
    return df.dropna(subset=['Date'])
