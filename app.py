import streamlit as st
import pandas as pd

st.title("Portfolio Dashboard")

data = {
    "Stock": ["AAPL", "NVDA", "TSLA"],
    "Buy": [1000, 2000, 1500],
    "Now": [1200, 2600, 1400]
}

df = pd.DataFrame(data)

df["Return %"] = (df["Now"] - df["Buy"]) / df["Buy"] * 100

st.dataframe(df)

total_buy = df["Buy"].sum()
total_now = df["Now"].sum()

return_rate = (total_now - total_buy) / total_buy * 100

st.metric("Total Return", f"{return_rate:.2f}%")
