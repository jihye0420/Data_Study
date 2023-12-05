import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
from io import BytesIO

with st.sidebar:
    st.header('회사와 기간을 입력하시오.')
    company = st.text_input('회사 이름')
    # st.text(company)

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
    # print("start_end_date: ", start_end_date)
    btn_start = st.button('주가 데이터 확인')


def get_stock_info():
    base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    url = "{0}?method={1}".format(base_url, method)
    # print(url)
    try:
        df = pd.read_html(url, header=0, encoding='cp949')[0]
        df['종목코드'] = df['종목코드'].apply(lambda x: f"{x:06d}")
        df = df[['회사명', '종목코드']]
    except Exception as e:
        print("e", e)
    return df


def get_ticker_symbol(company_name):
    df = get_stock_info()
    # print(df)
    code = df[df['회사명'] == company_name]['종목코드'].values
    ticker_symbol = code[0]
    return ticker_symbol


# 코드 조각 추가
if btn_start and company != '':
    st.header('무슨 주식을 사야 부자가 되려나...')
    stock_name = company
    date_range = start_end_date
    ticker_symbol = get_ticker_symbol(stock_name)
    start_p = date_range[0]
    end_p = date_range[1] + datetime.timedelta(days=1)
    df = fdr.DataReader(ticker_symbol, start_p, end_p, exchange="KRX")
    # st.text(df)
    # print(ticker_symbol)

    df.index = df.index.date
    st.subheader(f"[{stock_name}] 주가 데이터")
    st.dataframe(df.head())

    # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    # st.dataframe(px.line(df))
    # st.line_chart(df, x=[start_p.strftime("%Y-%m-%d"), end_p.strftime("%Y-%m-%d")], y='Close')

    st.line_chart(df, y='Close')

    # csv_download = st.button('CSV 파일 다운로드')
    # xlsx_download = st.button('엑셀 파일 다운로드')

    excel_data = BytesIO()
    csv_data = BytesIO()
    df.to_excel(excel_data)
    df.to_csv(csv_data)

    st.download_button("엑셀 파일 다운로드", excel_data, file_name='stock_data.xlsx')
    st.download_button("CSV 파일 다운로드", csv_data, mime="text/csv", file_name='stock_data.csv')
