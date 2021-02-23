import pandas as pd
from tiingo import TiingoClient

config={}

config["session"]= True
config["api_key"]= "00244882b421a2c0005d55ebb15e84dc2c03bb71"
client=TiingoClient(config)

""" historical_prices = client.get_ticker_price("SPY",
                                            fmt='json',
                                            startDate='2020-08-01',
                                            endDate='2021-02-18',
                                            frequency='daily')
print(type(historical_prices))
"""
ticker_metadata=client.get_ticker_metadata("SPY")
print(ticker_metadata)
