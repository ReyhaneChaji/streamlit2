import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

# تنظیمات Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open('ثبت نام دوره').sheet1

# عنوان و توضیحات فرم
st.title('فرم ثبت نام دوره')
st.write('لطفاً اطلاعات خود را برای ثبت نام در دوره وارد کنید.')

# فیلدهای فرم
name = st.text_input('نام')
email = st.text_input('ایمیل')
phone = st.text_input('شماره تلفن')
age = st.number_input('سن')

# دکمه ارسال
if st.button('ارسال'):
    # ذخیره اطلاعات در Google Sheets
    sheet.append_row([name, email, phone, age])

    # پیام تأیید
    st.success('با تشکر از ثبت نام شما!')

# نمایش لیست شرکت کنندگان
st.header('لیست شرکت کنندگان')
participants = sheet.get_all_records()
for participant in participants:
    st.write(f"{participant['نام']} - {participant['سن']} سال")

# استخراج داده های سنی
ages = [int(participant['سن']) for participant in participants]

# ایجاد نمودار سنی
plt.hist(ages)
plt.xlabel('سن')
plt.ylabel('تعداد شرکت کنندگان')
plt.title('نمودار سنی شرکت کنندگان')
st.pyplot()
