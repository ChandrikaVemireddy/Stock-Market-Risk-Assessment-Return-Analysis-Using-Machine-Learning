import numpy as np

def add_features(df):
    df = df.copy()
    df['Daily_Return'] = df['Close'].pct_change()
    df['Annual_Return'] = df['Close'].pct_change(252)
    df['Volatility'] = df['Daily_Return'].rolling(20).std() * np.sqrt(252)
    df['MA_10'] = df['Close'].rolling(10).mean()
    df['MA_20'] = df['Close'].rolling(20).mean()
    df['MA_50'] = df['Close'].rolling(50).mean()
    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df
