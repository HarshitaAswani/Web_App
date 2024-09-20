import streamlit as st
import yfinance as yf

# Define the ticker symbol for TCS and set the start and end dates
tcs = yf.Ticker("TCS.NS")  # Use "TCS.BO" for BSE or "TCS.NS" for NSE
start_date = "2013-01-01"
end_date = "2023-12-31"

# Fetch the historical data
df = tcs.history(period="1d", start=start_date, end=end_date)
df.drop(['Volume', 'Dividends', 'Stock Splits'], axis=1, inplace=True)

st.title('Stock Prices Visualization')
st.header('Tata Consultancy Services')
st.subheader('Open Price')
st.line_chart(df.Open)
st.subheader('Close Price')
st.line_chart(df.Close)
st.subheader('High Price')
st.line_chart(df.High)
st.subheader('Low Price')
st.line_chart(df.Low)