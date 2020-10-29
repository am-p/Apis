import pandas as pd
import requests


def getIntra(function, symbol, interval, size, token):

    url="https://www.alphavantage.co/query"
    parametros = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "outputsize": size,
        "apikey": token,
    }

    r=requests.get(url, params=parametros)
    data=r.json()["Time Series (" + interval + ")"]
    dataDF=pd.DataFrame.from_dict(data, orient="index")
    return dataDF

datos=getIntra("TIME_SERIES_INTRADAY","GGAL","1min","compact","H5EPS1VK18YSQ6WG")
print(datos)

TOKEN="H5EPS1VK18YSQ6WG"
def MACD(symbol, interval, series_type="close", fastperiod=12, slowperiod=26, signalperiod=9):

    function="MACD"
    url="https://www.alphavantage.co/query"
    parametros = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "series_type": series_type,
        "fastperiod": fastperiod,
        "slowperiod": slowperiod,
        "signalperiod": signalperiod,
        "apikey": TOKEN
    }

    r = requests.get(url, params=parametros)
    js = r.json()["Technical Analysis: MACD"]
    df = pd.DataFrame.from_dict(js, orient="index")
    df = df.astype("float")
    df.index.name = "Date"
    df = df.sort_values("Date", ascending=True).round(2)
    df.index = pd.to_datetime(df.index)
    return df


data = MACD("AAPL", "5min")
print(data)
