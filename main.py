import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px

st.title("Read Google Sheet as DataFrame")

# اتصال به گوگل شیت
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="1039332273",worksheet="Sheet2")

st.dataframe(df)

# فرم نظرسنجی
st.title("فرم نظرسنجی")

name = st.text_input("نام:")
family = st.text_input("نام خانوادگی:")
email = st.text_input("آدرس ایمیل:")
phone_number = st.text_input("شماره تماس:")

services = st.multiselect(
    "نوع خدمت دریافتی:",
    ["کاشت", "ترمیم", "مانیکور"]
)

feedback = st.text_area("نظر خود را بنویسید:")

# دکمه ارسال
if st.button('ارسال'):
    if name and family and email and phone_number and services and feedback:
        new_data = {
            'نام': name,
            'نام خانوادگی': family,
            'آدرس ایمیل': email,
            'شماره تماس': phone_number,
            'نوع خدمت دریافتی': ", ".join(services),
            'نظر': feedback
        }
        new_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_df], ignore_index=True)
        conn.update(data=df, worksheet="Sheet2")
        st.success('نظر شما با موفقیت ذخیره شد!')
    else:
        st.error('لطفاً تمام اطلاعات را وارد کنید.')

st.dataframe(df)

# ایجاد نمودار دایره‌ای برای نوع خدمات دریافتی
if not df.empty:
    services_count = df['نوع خدمت دریافتی'].str.get_dummies(sep=', ').sum()
    fig = px.pie(services_count, names=services_count.index, values=services_count.values, title='توزیع نوع خدمات دریافتی')
    st.plotly_chart(fig)
