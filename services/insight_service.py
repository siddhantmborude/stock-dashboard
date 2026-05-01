import numpy as np


def calculate_volatility(df):
    # Daily returns
    returns = df['Close'].pct_change().dropna()

    # Annualized volatility (%)
    volatility = np.std(returns) * np.sqrt(252) * 100

    return float(volatility)

def generate_signal(df):
    df = df.dropna()

    if len(df) < 20:
        return "HOLD"

    # Moving averages
    short_ma = df['Close'].rolling(5).mean().iloc[-1]
    long_ma = df['Close'].rolling(20).mean().iloc[-1]

    # Momentum (last 10 days)
    momentum = df['Close'].iloc[-1] - df['Close'].iloc[-10]

    # Volatility (use your updated function)
    volatility = calculate_volatility(df)

    if short_ma > long_ma and momentum > 0:
        return "BUY"

    elif short_ma < long_ma and momentum < 0:
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