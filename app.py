from fastapi import FastAPI
from services.data_service import fetch_stock_data
from services.insight_service import get_insights
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from services.ml_service import predict_price
from fastapi.responses import FileResponse



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COMPANIES = ["TCS", "INFY", "RELIANCE"]

@app.get("/")
def home():
    return FileResponse("index.html")







# 1. Companies list
@app.get("/companies")
def get_companies():
    return {"companies": COMPANIES}


# 2. Last 30 days data
@app.get("/data/{symbol}")
def get_data(symbol: str):
    df = fetch_stock_data(symbol)
    df = df.tail(30)

    return df.to_dict(orient="records")


# 3. Summary
@app.get("/summary/{symbol}")
def get_summary(symbol: str):
    df = fetch_stock_data(symbol)

    return {
        "symbol": symbol,
        "52w_high": float(df['Close'].max()),
        "52w_low": float(df['Close'].min()),
        "avg_close": float(df['Close'].mean())
    }


# 4. Insights (YOUR SPECIAL FEATURE 🔥)
@app.get("/insights/{symbol}")
def insights(symbol: str):
    df = fetch_stock_data(symbol)

    return get_insights(df, symbol)

@app.get("/predict/{symbol}")
def predict(symbol: str):
    df = fetch_stock_data(symbol)
    predicted_price = predict_price(df)

    return {
        "symbol": symbol,
        "predicted_price": predicted_price
    }


# 5. Compare (BONUS)
@app.get("/compare")
def compare(symbol1: str, symbol2: str):
    df1 = fetch_stock_data(symbol1)
    df2 = fetch_stock_data(symbol2)

    return {
        symbol1: float(df1['Close'].iloc[-1]),
        symbol2: float(df2['Close'].iloc[-1])
    }