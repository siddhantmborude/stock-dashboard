import numpy as np

def calculate_volatility(df):
    return np.std(df['Daily Return'].dropna())

def generate_signal(df):
    latest = df.iloc[-1]

    price = latest['Close']
    ma = latest['MA7']

    volatility = calculate_volatility(df)

    if price > ma and volatility < 0.02:
        return "BUY"
    elif price < ma and volatility > 0.03:
        return "SELL"
    else:
        return "HOLD"

def get_insights(df, symbol):
    volatility = calculate_volatility(df)
    signal = generate_signal(df)

    return {
        "symbol": symbol,
        "volatility_score": float(volatility),
        "signal": signal
    }   