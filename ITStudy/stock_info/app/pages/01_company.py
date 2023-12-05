import streamlit as st
import datetime
import streamlit as st

with st.sidebar:
    st.header('회사와 기간을 입력하시오.')
    company = st.text_input('회사 이름')
    st.text(company)

    today = datetime.datetime.now()
    today_year = today.year
    jan_1 = datetime.date(today_year, 1, 1)
    dec_31 = datetime.date(today_year, 12, 31)

    start_end_date = st.date_input(
        "시작일 - 종료일",
        (jan_1, datetime.date(today_year, 1, 7)),
        jan_1,
        dec_31,
        format="YYYY.MM.DD",
    )
