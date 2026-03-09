
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

def btc_5y_graph():
    btc = yf.Ticker("BTC-USD")
    df = btc.history(period="5y", interval="1d")
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='BTC/USD'
    ))

    fig.update_layout(
        title='BTC/USD - 5 Years',
        yaxis_title='$',
        xaxis_title='Date',
        
    )

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons = list([
            dict(count=7, label="1W", step="day", stepmode="backward"),
            dict(count=1, label="1M", step="month", stepmode="backward"),
            dict(count=3, label="3M", step="month", stepmode="backward"),
            dict(count=1, label="1Y", step="year", stepmode="backward"),
            dict(step="all", label="5Y")
            ])
        )
    )

    return fig