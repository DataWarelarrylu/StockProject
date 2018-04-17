import requests
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('oracle://lb:lb@192.168.1.30:1521/tsbi')
headers ={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
vcrdt = []
vcode = []
vtypes = []
vnumber = []
vprice = []

res = requests.get('http://quotes.money.163.com/hs/realtimedata/service/radar.php?host=/hs/realtimedata/service/radar.php&page=0&fields=CODE,PRICE,PERCENT,DATE,TYPES,SYMBOL,NUMBER,HSL&sort=DATE&order=desc&count=10000&type=query&callback=callback_2084078549&req=3166',headers=headers).text
v_res = eval(res.replace('callback_2084078549(','').replace(')',''))
# print(v_res)
for i in v_res['list']:
    a1 = eval(str(i))
    vcrdt.append(a1['DATE'])
    vcode.append(a1['CODE'])
    vtypes.append(a1['TYPES'])
    vnumber.append(a1['NUMBER'])
    vprice.append(a1['PRICE'])

data = {
'tcrdt':vcrdt,
'tcode':vcode ,
'ttypes':vtypes ,
'tnumber':vnumber ,
'tprice':vprice ,
}
df =pd.DataFrame(data)
print(df)
df.to_csv(r'D:\tmp\stock_wy\test.csv')
# df.to_sql('wy_scyd_v2', engine, if_exists='append', index=None)