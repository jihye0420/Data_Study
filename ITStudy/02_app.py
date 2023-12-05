import streamlit as st  # st는 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬이 담당
import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
data = df

# 입력
st.title('1. 입력버튼들')

button_result = st.button('Hit me1')
print(button_result)
# 버튼을 누르면 데이터 프레임이 등장하도록 로직을 만들기
if button_result:
    st.write(df)

# st.button('Hit me')
st.data_editor(data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose', 'ear'])
st.selectbox('Select', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1, '2'])

text_list = ['잔망루피1',
             '잔망루피2',
             '잔망루피3'
             ]
image_list = ['https://i.imgur.com/Pig3FpP.png',
              'https://i.imgur.com/7feD8We.png',
              'https://i.imgur.com/dBl9mmO.png',
              ]
search = st.text_input('Enter some text')

for tt in text_list:
    if search in tt:
        ii = text_list.index(tt)
if search != '':
    st.image(image_list[ii])

st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button(
    label="Download data as CSV",
    data=df.to_csv(),
    file_name='large_df.csv',
    mime='text/csv',
)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_')  # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects')  # df, err, func, keras!
st.write(['st', 'is <', 3])  # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True
