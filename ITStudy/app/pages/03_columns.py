import streamlit as st

# import 패키지 > 변수 > 함수 > 클래스 > 로직 작성 순서

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    st.write(add_selectbox)
    st.write(add_radio)

# Three columns with different widths
col1, col2, col3 = st.columns([3, 1, 1])  # 3:1:1 비율로 존재
# col1 is wider
col1.write('Column 1')
col2.write('Column 2')
col3.write('Column 3')

# Using 'with' notation:
with col1:
    st.image('https://i.imgur.com/Pig3FpP.png')
with col2:
    st.image('https://i.imgur.com/7feD8We.png')
with col3:
    st.image('https://i.imgur.com/dBl9mmO.png')
