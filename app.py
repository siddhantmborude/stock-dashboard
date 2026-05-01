from fastapi import FastAPI
from services.data_service import fetch_stock_data
from services.insight_service import get_insights
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from services.ml_service import predict_price
from fastapi.responses import FileResponse
import pandas as pd
from fastapi import Request
import traceback


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


@app.get("/data/{symbol}")
def get_data(symbol: str, days: int = 30):
    df = fetch_stock_data(symbol)

    if df is None or df.empty:
        return []

    return df.tail(days).to_dict(orient="records")
	

# 3. Summary
@app.get("/summary/{symbol}")
def get_summary(symbol: str):
    df = fetch_stock_data(symbol)

    if df is None or df.empty:
        return {"symbol": symbol, "52w_high": 0, "52w_low": 0, "avg_close": 0}

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

    if df is None or df.empty:
        return {"signal": "HOLD", "volatility_score": 0}

    try:
        return get_insights(df, symbol)
    except Exception as e:
        print("INSIGHTS ERROR:", e)
        return {"signal": "HOLD", "volatility_score": 0}

@app.get("/predict/{symbol}")
def predict(symbol: str):
    df = fetch_stock_data(symbol)

    if df is None or df.empty:
        return {"symbol": symbol, "predicted_price": 0}

    try:
        predicted_price = predict_price(df)
    except Exception as e:
        print("PREDICT ERROR:", e)
        predicted_price = 0

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


@app.get("/search")
def search_stock(query: str):
    try:
        df = pd.read_csv("nse_stocks.csv")

        # 🔥 CLEAN COLUMN NAMES (VERY IMPORTANT)
        df.columns = df.columns.str.strip().str.replace('\ufeff', '')

        print("Columns:", df.columns)  # debug

        result = df[
            df['Symbol'].str.contains(query.upper(), na=False) |
            df['Name'].str.contains(query, case=False, na=False)
        ]

        return result.head(10).to_dict(orient="records")

    except Exception as e:
        print("SEARCH ERROR:", e)
        return []

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("🔥 FULL ERROR:")
    traceback.print_exc()
    return {"error": str(exc)}