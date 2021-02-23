import pandas as pd
import requests

ticker = "SPY"
startDate = "2021-02-01"
resampleFreq = "1min"
#columns = "open,high,low,close,volume"
token = "00244882b421a2c0005d55ebb15e84dc2c03bb71"

urlBase = "https://api.tiingo.com/iex/SPY/prices"
# url=urlBase+"/<ticker>"+ticker
url = urlBase+"?&startDate="+startDate
url += "&resampleFreq="+resampleFreq
# url+="&columns"+columns
url += "&token="+token
print(url)
r = requests.get(url)
print(r)
