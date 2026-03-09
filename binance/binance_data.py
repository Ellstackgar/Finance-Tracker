from binance_client import client

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