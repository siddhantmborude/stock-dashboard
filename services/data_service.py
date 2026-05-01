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

        # 🔥 Fix MultiIndex
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()

        df = df[['Date', 'Open', 'Close']]

        # ✅ ADD THESE (VERY IMPORTANT)
        df['Daily Return'] = df['Close'].pct_change()
        df['MA7'] = df['Close'].rolling(7).mean()

        # ✅ Clean data properly
        df = df.dropna()

        return df

    except Exception as e:
        print("ERROR:", e)
        return pd.DataFrame()