import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("new title")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Sheet2", ttl=5 )

st.dataframe(df)
