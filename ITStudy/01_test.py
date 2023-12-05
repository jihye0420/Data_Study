import streamlit as st
import numpy as np
import pandas as pd

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

my_dataframe = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

st.dataframe(my_dataframe)
st.table(data[0:10])
st.json({'foo': 'bar', 'fu': 'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")

st.image('./잔망루피.jpeg')

# * optional kwarg unsafe_allow_html = True
# print("hello")
