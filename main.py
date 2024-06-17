# # this file added with compatible modules and codes
#
# import ssl
# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
#
# url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
#
# conn = st.connection("gsheets", type=GSheetsConnection)
#
# data = conn.read(spreadsheet=url, usecols=[0, 1])
# st.dataframe(data)

# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("new title")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Sheet2")

st.dataframe(df)
