import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

purchase = st.text_input('구매날짜 입력 (YYYY-MM-DD)')

if purchase:
    year = int(purchase.split('-')[0])
    month = int(purchase.split('-')[1])
    compare = datetime.strptime(str(year) + str(month), "%Y%m")  # 구매한 연, 월

    now = datetime.today()
    today_year = datetime.today().year  # 현재 연도 가져오기
    today_month = datetime.today().month  # 현재 월 가져오기

    purchase_date = datetime.strptime(purchase, "%Y-%M-%d")
    end_day = purchase_date + timedelta(days=1401)

    if today_year - year < 4:
        st.text(f"현재 {now - end_day}일이 남아 무료 업데이트 가능합니다.")
        if compare <= end_day:
            st.text("무료 업데이트 기간이 끝나갑니다. 빨리 업데이트를 진행하세요.")
    elif today_year - year >= 4:
        st.text("USB를 꽂아서 직접 업데이트하실래요 돈내고 온라인 업데이트 하실래요?")
