import requests
import pandas as pd


def historico(symbol, interval='1d', startTime=None, endTime=None, limit=1000):
    
    url = 'https://api.binance.com/api/v3/klines'
    
    params = {'symbol':symbol, 'interval':interval, 
              'startTime':startTime, 'endTime':endTime, 'limit':limit}
        
    r = requests.get(url, params=params)
    js = r.json()
    
    # Armo el dataframe
    cols = ['openTime','Open','High','Low','Close','Volume','cTime',
            'qVolume','trades','takerBase','takerQuote','Ignore']
    
    df = pd.DataFrame(js, columns=cols)
    
    #Convierto los valores strings a numeros
    df = df.apply(pd.to_numeric)
    
    # Le mando indice de timestamp
    df.index = pd.to_datetime(df.openTime, unit='ms')
    
    # Elimino columnas que no quiero
    df =df.drop(['openTime','cTime','takerBase','takerQuote','Ignore'],axis=1)
    df['vol_mln'] = df['qVolume'] / 10**6
    return df

historico('BTCUSDT', interval='2h', limit=10000)
