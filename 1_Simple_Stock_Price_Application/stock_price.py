import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price Application

Shown are the stock **closing price** & ***volume*** of Microsoft.

""")

#define the ticker symbol
tickerSymbol = 'MSFT'   

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

st.write("""
## Data
""")
tickerDf

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75