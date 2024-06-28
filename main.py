import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px
import gspread

st.title("لیست ثبت نامی ها ")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="1dof1Nl5ojO0woIp64OhwmYsw-VI-kFOO3ZMyy6zgcgI", worksheet="577754902")

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
        conn.update(spreadsheet="1dof1Nl5ojO0woIp64OhwmYsw-VI-kFOO3ZMyy6zgcgI",data=df, worksheet="Sheet3")
        st.success('اطلاعات شما با موفقیت ذخیره شد!')
    else:
        st.error('لطفاً تمام اطلاعات را وارد کنید.')


# --------------


st.title("نمودار جنسیت ثبت نامی‌ها")


gender_counts = df['جنسیت'].value_counts().reset_index()
gender_counts.columns = ['جنسیت', 'تعداد']


fig = px.pie(gender_counts, values='تعداد', names='جنسیت', title='توزیع جنسیت')
st.plotly_chart(fig)

# --------------

st.title("نمودار نوع دوره ثبت نامی‌ها")

course_counts = df['نوع دوره'].value_counts().reset_index()
course_counts.columns = ['نوع دوره', 'تعداد']

fig2 = px.bar(course_counts, x='نوع دوره', y='تعداد', title='توزیع نوع دوره')
st.plotly_chart(fig2)
