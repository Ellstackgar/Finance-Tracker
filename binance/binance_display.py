import pandas as pd
from binance_data import get_margin_orders, get_margin_trades
def to_dataframe(list):

    df = pd.DataFrame(list)
    return df

def margin_order_list():
    orders = get_margin_orders("BTCUSDT")

    list = to_dataframe(orders)
    list['actual_price'] = list.apply(
    lambda row: float(row['cummulativeQuoteQty']) / float(row['executedQty']) 
    if float(row['executedQty']) > 0 else 0,
    axis=1
    )   
    list = list.drop(columns=['price'])
    list = list.rename(columns={'actual_price': 'price'})
    list = list[['symbol', 'side', 'type', 'price', 'origQty', 'executedQty', 'status', 'time']]
    list['time'] = pd.to_datetime(list['time'], unit='ms')


    return list