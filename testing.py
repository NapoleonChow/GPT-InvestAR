from openbb import obb
import pandas as pd

obb.account.login(pat="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3Rva2VuIjoiN2JPdFZFVmNCNFlWU1QyMHlEUGt1YUo4Q1JmQmVHdzVsUEs0VG5HRSIsImV4cCI6MTc0MzAwMTMxOH0.MmTfy4X3KLu3TuenHXH9G78kCgeMVYlC2gjhzqvAP8c")
symbol='BCC'
start_date='2002-01-01'
end_date='2023-12-31'
price_data = obb.equity.price.historical(symbol=symbol, start_date=start_date, end_date=end_date, provider='fmp')
price_data_sp500 = obb.equity.price.historical(symbol="^GSPC", start_date=start_date, end_date=end_date, provider='fmp')
full_df = pd.DataFrame()
stock = price_data.to_df()
# historical_prices = obb.equity.price.historical("AAPL", provider='alpha_vantage')
print(stock.head(5))

"""
             open   high    low  close    volume   vwap  adj_close  unadjusted_volume  change  change_percent
date
2013-02-06  25.44  26.75  25.25  26.15  13195500  26.05      18.49         13195500.0    0.71        0.027900
2013-02-07  26.25  27.49  26.25  27.29   1290800  27.01      19.29          1290800.0    1.04        0.039600
2013-02-08  27.68  28.08  27.04  27.56    734200  27.56      19.48           734200.0   -0.12       -0.004335
2013-02-11  27.50  27.50  26.27  27.15    686000  26.97      19.19           686000.0   -0.35       -0.012700
2013-02-12  26.75  27.54  26.50  27.48    559600  27.17      19.43           559600.0    0.73        0.027300
"""