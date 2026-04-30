# 📊 Stock Intelligence Dashboard

A full-stack stock analysis dashboard that provides real-time insights, comparison tools, and machine learning–based price prediction.

---

## 🚀 Overview

The **Stock Intelligence Dashboard** is a web-based application that allows users to:

* Visualize stock price trends 📈
* Compare multiple stocks 🔁
* Analyze volatility 📊
* Get Buy/Sell/Hold signals 🟢🔴
* Predict future stock prices using ML 🤖

This project demonstrates **data processing, API development, visualization, and machine learning integration** in a single application.

---

## ✨ Features

### 📈 Stock Visualization

* Interactive line charts using Chart.js
* Displays recent stock price trends

### 🔁 Stock Comparison

* Compare two stocks on the same chart
* Helps identify better-performing assets

### 📅 Time Filters

* Last 30 days
* Last 90 days

### 📊 Volatility Analysis

* Calculates standard deviation of daily returns
* Categorized into Low / Medium / High

### 🟢 Signal Generation

* BUY / SELL / HOLD based on:

  * Moving average
  * Volatility

### 🤖 ML Price Prediction

* Predicts next-day price using Linear Regression
* Uses last 5 days of historical data

### 🎨 Modern UI

* Clean dashboard design
* Light/Dark theme styling
* Responsive layout

---

## 🛠️ Tech Stack

### 🔹 Backend

* FastAPI
* Pandas
* NumPy
* yfinance

### 🔹 Machine Learning

* Scikit-learn (Linear Regression)

### 🔹 Frontend

* HTML, CSS, JavaScript
* Chart.js

### 🔹 Deployment

* Render (Backend hosting)
* GitHub (Version control)

---

## 📂 Project Structure

```
stock-dashboard/
│
├── app.py
├── requirements.txt
├── index.html
│
└── services/
    ├── data_service.py
    ├── insight_service.py
    └── ml_service.py
```

---

## ⚙️ How It Works

### 1. Data Collection

* Fetches stock data using `yfinance`
* Uses 1-year historical data

### 2. Data Processing

* Handles missing values
* Converts date formats
* Calculates:

  * Daily Return
  * 7-day Moving Average
  * 52-week High/Low

### 3. Insights Engine

* Computes volatility
* Generates Buy/Sell/Hold signal

### 4. ML Model

* Uses last 5 closing prices
* Trains Linear Regression model
* Predicts next-day price

### 5. Visualization

* Displays:

  * Stock price chart
  * Comparison chart
  * Prediction line

---

## ▶️ Run Locally

### 1. Clone repository

```bash
git clone https://github.com/siddhantmborude/stock-dashboard.git
cd stock-dashboard
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run backend

```bash
uvicorn app:app --reload
```

### 5. Open frontend

* Open `index.html` in browser

---

## 🌐 Live Demo

👉 https://stock-dashboard-vsl1.onrender.com

---

## 📌 API Endpoints

| Endpoint             | Description           |
| -------------------- | --------------------- |
| `/companies`         | List available stocks |
| `/data/{symbol}`     | Get stock data        |
| `/summary/{symbol}`  | Summary stats         |
| `/insights/{symbol}` | Volatility + signal   |
| `/predict/{symbol}`  | ML prediction         |

---

## ⚠️ Notes

* Data is fetched using `yfinance` (near real-time, slight delay)
* ML model is basic and for demonstration purposes
* Not intended for financial decision-making

---

## 🔮 Future Improvements

* Candlestick charts 📊
* Real-time streaming data ⏱️
* Advanced ML models (LSTM, ARIMA)
* User authentication 🔐
* Portfolio tracking

---

## 👨‍💻 Author

Siddhant Borude

---

## ⭐ Conclusion

This project demonstrates:

* Full-stack development
* Data analysis
* Machine learning integration
* UI/UX design

👉 Designed to simulate a **real-world financial analytics tool**.
