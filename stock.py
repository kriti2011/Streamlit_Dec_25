import streamlit as st
import yfinance as yf
import datetime
st.title("Stock Price Predictor")
st.subheader("Analyze and visualize stock prices over time")

col1,col2,col3=st.columns(3)

with col1:
    company=st.text_input("Company Ticker","MSFT")

with col2:
    sd=st.date_input("Start Date",datetime.date(2025, 1, 1))

with col3:
    ed=st.date_input("End Date", datetime.date(2025, 12, 31))


ticker=yf.Ticker(company)
ticker_data=ticker.history(start=sd, end=ed)

st.write("Stock data", f"({company})")
st.dataframe(ticker_data.head())


st.write("Price movement over time", f"({company})")
st.line_chart(ticker_data['Close'])

st.write("Volume traded over time", f"({company})")
st.bar_chart(ticker_data['Volume'])







