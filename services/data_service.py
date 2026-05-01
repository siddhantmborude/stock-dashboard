import yfinance as yf
import pandas as pd
import datetime

def fetch_stock_data(symbol: str):

    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=365)

    df = yf.download(symbol + ".NS", start=start, end=end)

    if df.empty:
        return pd.DataFrame(columns=["Date", "Open", "Close"])

    df.reset_index(inplace=True)

    df = df[['Date', 'Open', 'Close']]

    df = df.dropna()

    df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']
    df['MA7'] = df['Close'].rolling(window=7).mean()

    df['52W_High'] = df['Close'].rolling(window=252).max()
    df['52W_Low'] = df['Close'].rolling(window=252).min()

    df = df.fillna(0)

    return df