import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_price(df):
    df = df.dropna()

    closes = df['Close'].values

    X = []
    y = []

    for i in range(5, len(closes)):
        X.append(closes[i-5:i])
        y.append(closes[i])

    X = np.array(X)
    y = np.array(y)

    model = LinearRegression()
    model.fit(X, y)

    last_5 = closes[-5:].reshape(1, -1)
    prediction = model.predict(last_5)[0]

    return float(prediction)