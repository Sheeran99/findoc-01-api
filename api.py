from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

# 定义一个接口：当有人访问网站根路径“/”时，返回这段内容
@app.get("/")

def read_root():
    return{"message":"你好,这是我的第一个API"}

# 新接口：访问 /stock/股票代码 时，返回该股票的涨跌数据
@app.get("/stock/{symbol}")

def get_stock(symbol: str):
    stock = yf.Ticker(symbol)
    history = stock.history(period = "1mo")

    first_close = history["Close"].iloc[0]
    last_close = history["Close"].iloc[-1]
    change = last_close - first_close
    change_percent = (change/first_close) * 100
    return {
        "symbol":symbol,
        "first_close":round(first_close,2),
        "last_close":round(last_close,2),
        "change":round(change,2),
        "change_percent":round(change_percent,2)
    }