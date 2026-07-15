import yfinance as yf
import streamlit as st
import datetime

st.write("""
# Simple Stock Price App

Show the stock closing price and volume of your selection!

""")

sd = st.date_input("Start date", datetime.date(2010,5,31))

ed = st.date_input("End date")

option = st.selectbox('Enter the Stock symbol', ('AAPL','TSLA','GOOG','MSFT','1211.HK','0005.HK'))

#define the ticker symbol
tickerSymbol = option

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = yf.download(tickerSymbol, sd, ed)
tickerDf.columns = tickerDf.columns.droplevel(1)

# Open	High	Low	Close	Volume	Dividends	Stock Splits

tickerDf['simple_rtn'] = tickerDf.Close.pct_change()
Company_Name = "APPLE Inc"
if option == "AAPL":
    Company_Name == "APPLE Inc."
elif option == "TSLA":
    Company_Name = "Tesla, Inc."
elif option == "MSFT":
    Company_Name = "Microsoft Corporation"
elif option == "GOOG":
    Company_Name = "Alphabet Inc."
elif option == "1211.HK":
    Company_Name = "BYD Company Limited"
else :
    Company_Name = "HSBC Holdings plc"

#stock_dict = {"AAPL": "APPLE Inc.", 
#                   "TSLA": "Tesla, Inc.", 
#                   "GOOG": "Alphabet Inc.", 
#                   "MSFT": "Microsoft Corporation", 
#                   "0005.HK": "HSBC Holdings plc", 
#                   "1211.HK": "BYD Company Limited"}
#Company_Name = stock_dict[tickerSymbol]

#tickerData = yf.Ticker(tickerSymbol)
#company_name = tickerData.info['longName']

st.write("""# """ + Company_Name + """
# Stock close Price
""")
st.line_chart(tickerDf.Close)
st.write("""# """ + Company_Name + """
# Stock Daily Volumn
""")
st.line_chart(tickerDf.Volume)
st.write("""# """ + Company_Name + """
# Stock Simple Return
""")
st.line_chart(tickerDf.simple_rtn)