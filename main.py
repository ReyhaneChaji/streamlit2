import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px

st.title("لیست ثبت نامی ها ")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="ثبت نام دوره")

st.dataframe(df)

# --------------

st.title('فرم ثبت نام در دوره استریم لیت')
st.info('لطفاً اطلاعات خود را در این فرم وارد کنید.')

name = st.text_input('نام:')
family = st.text_input('نام خانوادگی:')
phone_number = st.text_input('شماره تماس:')
course_type = st.selectbox('نوع دوره:', ['حضوری', 'غیر حضوری'])
gender = st.selectbox('جنسیت:', ['مرد', 'زن', 'سایر'])

# دکمه ارسال
if st.button('ارسال'):
    if name and family and phone_number and course_type and gender:
        new_data = {
            'نام': name,
            'نام خانوادگی': family,
            'شماره تماس': phone_number,
            'نوع دوره': course_type,
            'جنسیت': gender
        }
        new_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_df], ignore_index=True)
        conn.update(data=df, worksheet="ثبت نام دوره")
        st.success('اطلاعات شما با موفقیت ذخیره شد!')
    else:
        st.error('لطفاً تمام اطلاعات را وارد کنید.')

# --------------

# رسم نمودار دایره‌ای بر اساس جنسیت
st.title("نمودار جنسیت ثبت نامی‌ها")

# شمارش تعداد افراد بر اساس جنسیت
gender_counts = df['جنسیت'].value_counts().reset_index()
gender_counts.columns = ['جنسیت', 'تعداد']

# رسم نمودار با Plotly
fig = px.pie(gender_counts, values='تعداد', names='جنسیت', title='توزیع جنسیت')
st.plotly_chart(fig)

# --------------

# رسم نمودار ستونی بر اساس نوع دوره
st.title("نمودار نوع دوره ثبت نامی‌ها")

# شمارش تعداد افراد بر اساس نوع دوره
course_counts = df['نوع دوره'].value_counts().reset_index()
course_counts.columns = ['نوع دوره', 'تعداد']

# رسم نمودار ستونی با Plotly
fig2 = px.bar(course_counts, x='نوع دوره', y='تعداد', title='توزیع نوع دوره')
st.plotly_chart(fig2)
