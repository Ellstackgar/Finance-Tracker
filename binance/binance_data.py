from binance_client import client
from datetime import datetime, timedelta, timezone
import time

def get_balances():
    account = client.get_account()
    margin_account = client.get_margin_account()

    spot = [b for b in account['balances'] if float(b['free']) > 0 or float(b['locked']) > 0]
    margin = [a for a in margin_account['userAssets'] if float(a['free']) > 0 or float(a['borrowed']) > 0 or float(a['interest']) > 0]
    
    # make list of balances
    all_holdings = (
        [{'asset': b['asset'], 'free': b['free'], 'locked': b['locked']} for b in spot] +
        [{'asset': a['asset'], 'free': a['netAsset'], 'locked': '0'} for a in margin]
    )

    return all_holdings

def get_margin_trades(symbol, period='1w'):
    
    now = datetime.now(timezone.utc)
    
    # calculate start time based on period
    if period == '1d':
        start = now - timedelta(days=1)
    elif period == '1w':
        start = now - timedelta(weeks=1)
    elif period == '1m':
        start = now - timedelta(days=30)
    else:
        raise ValueError(f"Unknown period: {period}")
    
    # convert to millisecond timestamp — binance requires this
    start_ms = int(start.timestamp() * 1000)
    
    trades = client.get_margin_trades(
        symbol=symbol,
        startTime=start_ms,
        isIsolated='FALSE'  # FALSE = cross margin
    )
    
    return trades

def get_margin_orders(symbol, period='1w'):
    
    now = datetime.now(timezone.utc)
    
    if period == '1d':
        start = now - timedelta(days=1)
    elif period == '1w':
        start = now - timedelta(weeks=1)
    elif period == '1m':
        start = now - timedelta(days=30)

    start_ms = int(start.timestamp() * 1000)
    
    orders = client.get_all_margin_orders(
        symbol=symbol,
        startTime=start_ms,
        isIsolated='FALSE'
    )
    
    return orders