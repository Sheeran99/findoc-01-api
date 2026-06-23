import yfinance as yf

def get_stock_change(symbol,period = "1mo"):
    #查询某只股票在一段时间内的涨跌情况
    stock = yf.Ticker(symbol)
    history = stock.history(period = period)

    first_close = history["Close"].iloc[0]
    last_close = history["Close"].iloc[-1]
    change = last_close - first_close
    change_percent = (change/first_close)*100

    print(f"股票代码：{symbol}")
    print(f"期初收盘：{first_close:.2f}")
    print(f"期末收盘：{last_close:.2f}")
    print(f"涨跌额：{change:.2f}")
    print(f"涨跌幅：{change_percent:.2f}%")
    print("-" * 30)

get_stock_change("SPCX","5d")