from binance_client import client

## converts cryptocurrencies to GBP
def get_portfolio_values(all_holdings):
   
    results = []

    # approximate GBP rate for USD stablecoins
    gbp_usd = float(client.get_symbol_ticker(symbol="GBPUSDT")['price'])

    for holding in all_holdings:
        asset = holding['asset']
        amount = float(holding['free']) + float(holding['locked'])
    
        try:
            # try direct GBP pair first
            ticker = client.get_symbol_ticker(symbol=f"{asset}GBP")
            price = float(ticker['price'])
            value = amount * price
        except:
        
            try:
                # fall back to USDT pair, convert to GBP
                ticker = client.get_symbol_ticker(symbol=f"{asset}USDT")
                price = float(ticker['price']) / gbp_usd
                value = amount * price
            except:

                try:
                    # some stablecoins ARE usdt/gbp equivalent
                    if asset in ['USDT', 'USDC', 'BUSD', 'DAI']:
                        value = amount / gbp_usd
                    else:
                        value = None
                except:
                    value = None

        results.append({
        'coin': asset,
        'amount': amount,
        'value_gbp': value
        })

    return results