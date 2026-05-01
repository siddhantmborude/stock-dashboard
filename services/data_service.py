import yfinance as yf
import pandas as pd
import datetime

def fetch_stock_data(symbol: str):
    try:
        end = datetime.datetime.today()
        start = end - datetime.timedelta(days=365)

        df = yf.download(symbol + ".NS", start=start, end=end)

        if df is None or df.empty:
            return pd.DataFrame()

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()

        df = df[['Date', 'Open', 'Close']]

        # ✅ Metrics
        df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']
        df['MA7'] = df['Close'].rolling(7).mean()
        df['52W_High'] = df['Close'].expanding().max()
        df['52W_Low'] = df['Close'].expanding().min()

        # Keep valid rows
        df = df.dropna(subset=['Open', 'Close'])

        # Fill indicators
        df['MA7'] = df['MA7'].bfill()
        df['52W_High'] = df['52W_High'].bfill()
        df['52W_Low'] = df['52W_Low'].bfill()

        # 🔥 CRITICAL FIX (JSON ERROR)
        df = df.replace([float('inf'), -float('inf')], 0)
        df = df.fillna(0)

        return df

    except Exception as e:
        print("DATA ERROR:", e)
        return pd.DataFrame()