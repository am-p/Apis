import requests
import pandas as pd

def obtenerHora():
    endpoint="https://api.kraken.com/0/public/Time"
    #p={"unixtime":1604274542,"rfc1123":"Sun,  1 Nov 20 23:49:02 +0000"}
    r=requests.get(url=endpoint)
    return r.json()



def infoActivo():
    endpoint="https://api.kraken.com/0/public/Assets"
    r=requests.get(url=endpoint)
    return r.json()


date=obtenerHora()    
print(date["result"]["rfc1123"])
info=infoActivo()
print(info)

