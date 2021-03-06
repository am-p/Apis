import pandas as pd, requests
import matplotlib.pyplot as plt

apikey="H5EPS1VK18YSQ6WG"

def RSI(symbol, interval, series_type, time_period):
    function='RSI'
    url='https://www.alphavantage.co/query'
    parametros={'function':function, 'symbol':symbol, 'interval':interval, 
                  'series_type':series_type,'time_period':time_period ,'apikey':apikey}
    r=requests.get(url, params=parametros)
    js=r.json()['Technical Analysis: RSI']
    df=pd.DataFrame.from_dict(js, orient='index')
    df=df.astype('float')
    df.index.name='Date'
    df=df.sort_values('Date',ascending=True).round(2)
    df.index=pd.to_datetime(df.index)    
    return df

def MACD(symbol, interval, series_type='close', fastperiod=12, slowperiod=26, signalperiod=9):
    function='MACD'
    url='https://www.alphavantage.co/query'
    parametros = {'function':function, 'symbol':symbol, 'interval':interval, 
                  'series_type':series_type, 'fastperiod': fastperiod, 
                  'slowperiod':slowperiod, 'signalperiod':signalperiod,
                  'apikey':apikey }
    r=requests.get(url, params=parametros)
    js=r.json()['Technical Analysis: MACD']
    df=pd.DataFrame.from_dict(js, orient='index')
    df=df.astype('float')
    df.index.name='Date'
    df=df.sort_values('Date', ascending=True).round(2)
    df.index=pd.to_datetime(df.index)    
    return df

def getDailyAdj(symbol, size):
    function='TIME_SERIES_DAILY_ADJUSTED'
    url='https://www.alphavantage.co/query'
    parametros={'function' : function, 'symbol': symbol, 
                  'outputsize': size, 'apikey': apikey}
    r=requests.get(url, params=parametros)
    data=r.json()['Time Series (Daily)']
    dataDF=pd.DataFrame.from_dict(data, orient='index')
    dataDF=dataDF.astype('float')
    dataDF.index.name='Date'
    dataDF.columns=['Open','High','Low','Close','AdjClose','Volume','Div','Split']
    dataDF=dataDF.sort_values('Date', ascending=True).round(2)
    dataDF.index=pd.to_datetime(dataDF.index)    
    return dataDF

symbol = 'MELI'
rsi = RSI(symbol,'daily','close', 14)
macd = MACD(symbol,'daily')
precios = getDailyAdj(symbol=symbol, size='full')

tabla = pd.concat([precios.Close,macd,rsi],axis=1).dropna()
#print(tabla)
data = tabla.loc[tabla.index>'2019'].copy()
data['Buy'] = (data.MACD_Hist>0)&(data.MACD_Hist.shift()<0)
data['Sell'] = (data.MACD_Hist<0)&(data.MACD_Hist.shift()>0)

#graficos
fig, ax = plt.subplots(figsize=(12,12), nrows=3)
ax[0].plot(data.index, data.Close, label='Precio Close', c='k')

ax[1].plot(data.index, data.MACD, label='MACD Fast', ls='--', color='red')
ax[1].plot(data.index, data.MACD_Signal, label='MACD Slow', color='green')
ax[1].bar(data.index, data.MACD_Hist, color='gray', label='MACD Signal')

ax[2].plot(data.index, data.RSI, label='RSI Index')
ax[2].axhline(y=70, xmin=0, color='gray', linestyle='--')
ax[2].axhline(y=30, xmin=0, color='gray', linestyle='--')

for i in range(3):
    ax[i].legend(loc='upper left',bbox_to_anchor=(1, 1), frameon=True)


buySig = data.MACD.loc[data.Buy==True]
sellSig = data.MACD.loc[data.Sell==True]
ax[1].plot(buySig.index, buySig, "^", markersize=15, c='g')
ax[1].plot(sellSig.index, sellSig, "v", markersize=15, c='r')

for idx, row in data.iterrows():
    rango = data.Close.max()-data.Close.min()
    h = (row.Close-data.Close.min())/rango
    if row.Buy==True:
        ax[0].axvline(x=idx, ymin=0, ymax=h , c='green')
    if row.Sell:
        ax[0].axvline(x=idx, ymin=0, ymax=h, c='red', ls="--")

plt.subplots_adjust(hspace=0)

print(data)
plt.show()
