from cad_tickers.exchanges.tsx.get_ticker_data import get_ticker_data   
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import time
# TOCO read data file and produce another csv that contains this graphql ticker data

data_csv = pd.read_csv("data/us.csv")


def get_tmx_name(code, ex):
    # print(code, ex)
    return f"{code}:US"
    # map data from us tickers to something useful

print(len(data_csv))
# data_csv = data_csv.dropna(subset=['Exchange'])
data_csv['tmx_name'] = data_csv.apply(lambda x: get_tmx_name(x["Code"], x["Exchange"]), axis=1)

us_stocks = data_csv["tmx_name"].tolist()
print(len(us_stocks))
def get_data(symbol=str):
    time.sleep(0.2)
    return get_ticker_data(symbol)

ticker_data = []
for stock in us_stocks:
    ticker_data.append(get_ticker_data(stock))

# using list comprehension
# to remove None values in list
ticker_data = [i for i in ticker_data if i]

ticker_df = pd.DataFrame(ticker_data)

ticker_df.to_csv("data/us_stock_data.csv")
