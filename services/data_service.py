import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol: str):
    stock = yf.Ticker(symbol + ".NS")
    df = stock.history(period="1y")

    df.reset_index(inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])

    df = df[['Date', 'Open', 'Close']]

    df = df.dropna()

    df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']

    df['MA7'] = df['Close'].rolling(window=7).mean()

    df['52W_High'] = df['Close'].rolling(window=252).max()
    df['52W_Low'] = df['Close'].rolling(window=252).min()

    # 🔥 IMPORTANT FIX
    df = df.fillna(0)

    return df