import yfinance as yf
import streamlit as st
import datetime



st.write("""
# Simple Stock Price App

Shown stock closing price and volume of the stock!

""")

sd = st.date_input("Start date", datetime.date(2010,1,30))

ed = st.date_input("End date")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

option = st.selectbox('Enter the Stock symbol', ('AAPL','TSLA','GOOG','MSFT','1211.HK','0005.HK'))

tickerSymbol = option
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')
tickerDf = yf.download(tickerSymbol,sd,ed)
tickerDf.columns = tickerDf.columns.droplevel(1)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
company_name = tickerData.info['longName']

st.markdown(f"<p style='font-size: 24px;'>Company {company_name}</p>", unsafe_allow_html=True)


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)