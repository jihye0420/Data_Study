import streamlit as st
from PIL import Image

charic_list = ['잔망1', '잔망2', '잔망3']
image_files = ['잔망루피1.png', '잔망루피2.png', '잔망루피3.png']

img1 = Image.open('./data/' + '잔망루피1.png')
img2 = Image.open('./data/' + '잔망루피2.png')
img3 = Image.open('./data/' + '잔망루피3.png')

t = st.radio('Pick one:', charic_list)
if t == '잔망1':
    st.image(img1)
elif t == '잔망2':
    st.image(img2)
elif t == '잔망3':
    st.image(img3)

# charic_list = ['잔망1', '잔망2', '잔망3']
# image_files = ['잔망루피1.png', '잔망루피2.png', '잔망루피3.png']

ani = st.selectbox('Select', [0, 1, 2])
img = Image.open('./data/' + image_files[ani])
st.image(img)

# 특정 단어가 검색되면 그 검색어 기준으로 이미지 파일을 찾아주세요
ani = st.text_input('Enter some text', placeholder=None)

for ww in charic_list:
    if ani in ww:
        img = Image.open('./data/' + image_files[charic_list.index(ww)])  # 이러면 아무것도 입력 안했을 때, 모든 사진이 뜸

if ani != '':
    st.image(img)

# """
# import streamlit as st
# from PIL import Image
#
# # 입력창의 값에 따라 두 개의 리스트를 하나의 자료처럼 관리
# ani_list = ['짱구는 못말려', '몬스터', '릭앤모티']
# image_files = ['jjanggu.png', 'monster.png', 'rickandmorty.jpg']
#
# ani = st.radio('Pick one:', ani_list)
# img_idx = ani_list.index(ani)
# img = Image.open('./data/'+image_files[img_idx])
#
# st.image(img)
#
#
# ani_list = ['짱구는 못말려', '몬스터', '릭앤모티']
# image_files = ['jjanggu.png', 'monster.png', 'rickandmorty.jpg']
#
# ani = st.selectbox('Select', ani_list)
# img_idx = ani_list.index(ani)
# img = Image.open('./data/'+image_files[img_idx])
#
# ani_list = ['짱구는 못말려', '몬스터', '릭앤모티']
# image_files = ['jjanggu.png', 'monster.png', 'rickandmorty.jpg']
#
# ani = st.selectbox('Select', [0, 1, 2])
# img = Image.open('./data/'+image_files[ani])
#
# st.image(img)
#
# # 특정 단어가 검색되면 그 검색어 기준으로 이미지 파일을 찾아주세요
# ani = st.text_input('Enter some text')
# """
# st.button('Hit me')
# st.data_editor('Edit data', data)
# st.checkbox('Check me out')
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.download_button('On the dl', data)
# st.camera_input("一二三,茄子!")
# st.color_picker('Pick a color')
