import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import json

# 데이터 불러오기
file_path = "/Users/hwangjihye/jihye/Data_Study/ITStudy/youtube/KR_category_id.json"

df = pd.read_csv('/Users/hwangjihye/jihye/Data_Study/ITStudy/youtube/KR_youtube_trending_data_korean.csv',
                 encoding='utf-8')


def json_to_dict():
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


with st.sidebar:
    data = json_to_dict()
    item_list = data['items']
    tt = {}  # id = title

    for i in item_list:
        tt[int(i['id'])] = i['snippet']['title']
    print("tt", tt)
    st.text('카테고리 아이디 - 카테고리')
    st.write(tt)

st.title("YOUTUBE 인기 동영상과 관련한 데이터 분석")
# 1. 어떤 카테고리의 동영상이 가장 많이 인기를 얻었는지 확인
st.header("1. 카테고리별 동영상 수 (Matplotlib & Seaborn)")
# categoryId' 컬럼을 기준으로 각 카테고리별 동영상 수를 계산
category_popularity = df['categoryId'].value_counts().sort_values(ascending=False)

# json을 읽어와서 카테고리 id와 매핑하는 과정
data = json_to_dict()
item_list = data['items']
temp = []  #
tt = {}  # id = title

for i in item_list:
    tt[int(i['id'])] = i['snippet']['title']

for c in category_popularity.index:
    if c in tt.keys():
        temp.append(tt[c])
    else:
        temp.append("기타")

# print("temp: ", temp)
# print(len(temp))
# print(category_popularity.index)
# print(category_popularity.values)
# print(len(category_popularity.values))

# Matplotlib의 figure 함수를 사용하여 그림의 크기를 설정
plt.figure(figsize=(10, 6))
# Seaborn의 barplot 함수를 사용하여 막대 그래프
# sns.barplot(x=category_popularity.index, y=category_popularity.values, palette='viridis')
sns.barplot(x=temp, y=category_popularity.values, palette='viridis')
plt.title('카테고리별 동영상 수')
plt.xlabel('카테고리')
plt.ylabel('동영상 수')
plt.rc('font', family='AppleGothic')
plt.xticks(rotation=45)
st.pyplot(plt)
st.text("가장 많은 동영상의 수는 예능, 사람(브이로그), 음악 과 같은 카테고리를 가진 동영상입니다.")

# 2. 카테고리별 좋아요와 싫어요 수의 평균 및 비율 계산
st.header("2. 카테고리 별 좋아요, 싫어요 평균 및 비율 (Matplotlib & Seaborn)")
# 좋아요/싫어요 수의 평균 및 비율 계산
average_likes_dislikes = df.groupby('categoryId')[['likes', 'dislikes']].mean()
average_likes_dislikes['likes_to_dislikes_ratio'] = average_likes_dislikes['likes'] / average_likes_dislikes['dislikes']

# 평균 및 비율 데이터프레임 출력
st.dataframe(average_likes_dislikes)

# 세로 막대 그래프
st.header("카테고리별 좋아요 및 싫어요 평균 수 (로그 스케일)")
fig, ax = plt.subplots(figsize=(10, 6))

# 좋아요, 싫어요 평균 그래프 (로그 스케일)
sns.barplot(x=average_likes_dislikes.index, y='likes', data=average_likes_dislikes, color='green',
            label='좋아요', ax=ax)
sns.barplot(x=average_likes_dislikes.index, y='dislikes', data=average_likes_dislikes, color='red',
            label='싫어요', ax=ax)
ax.set_yscale('log')  # 로그 스케일 적용
ax.set_xlabel('카테고리')
ax.set_ylabel('평균 수 (로그 스케일)')
ax.set_title('카테고리별 좋아요 및 싫어요 평균 수 (로그 스케일)')
ax.legend()

# 그래프 시각화
st.pyplot(fig)
st.text("각 카테고리의 좋아요와 싫어요 평균, 그리고 좋아요와 싫어요 비율을 보여줍니다.")

# 3.
# 게시 시간대 분석:
# 동영상이 게시된 시간대에 따라 좋아요/싫어요 수의 차이를 분석합니다.
# 특정 시간대에 게시된 동영상이 더 많은 좋아요를 받는지 확인
st.header("3. 게시된 시간대에 따라 좋아요/싫어요 수의 차이")

# 'publishedAt' 컬럼을 datetime 형식으로 변환
df['publishedAt'] = pd.to_datetime(df['publishedAt'])

# 'hour' 컬럼을 추가하여 시간대 추출
df['hour'] = df['publishedAt'].dt.hour
# print(df['hour'])
# 좋아요/싫어요 수의 평균 계산
likes_dislikes_by_hour = df.groupby('hour')[['likes', 'dislikes']].mean().reset_index()

# 시각화
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='likes', data=likes_dislikes_by_hour, label='좋아요', marker='o')
sns.lineplot(x='hour', y='dislikes', data=likes_dislikes_by_hour, label='싫어요', marker='o')
plt.title('게시 시간대별 동영상 좋아요 및 싫어요 평균 수')
plt.xlabel('게시 시간대 (24시간)')
plt.ylabel('평균 수')
plt.legend()

# 그래프를 Streamlit에 표시
st.pyplot(plt)
st.text("동영상이 게시된 시간대에 따라 좋아요/싫어요 수의 차이를 분석해보니, 13시에 가장 많이 좋아요를 누르는 시간대로 보입니다.")

# 4. 댓글 수와의 관계 분석:
# 동영상의 댓글 수와 좋아요/싫어요 수 간의 상관 관계를 조사합니다.
# 댓글이 많은 동영상일수록 좋아요/싫어요가 높은 경향이 있는지 확인
# 좋아요/싫어요 수 간의 산점도가 생성되고, 상관 계수가 출력됩니다. 상관 계수는 -1에서 1까지의 값을 가지며, 1에 가까울수록 강한 양의 상관 관계
st.header("4. 동영상의 댓글 수와 좋아요/싫어요 수 상관 관계 분석")
# 댓글 수와 좋아요/싫어요 수의 상관 관계 분석
correlation_comments_likes = df['comment_count'].corr(df['likes'])
correlation_comments_dislikes = df['comment_count'].corr(df['dislikes'])

# 산점도 시각화
# st.title('댓글 수와 좋아요/싫어요 수의 상관 관계 (Seaborn)')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='comment_count', y='likes', data=df, label='좋아요', alpha=0.7, ax=ax)
sns.scatterplot(x='comment_count', y='dislikes', data=df, label='싫어요', alpha=0.7, ax=ax)
plt.title('댓글 수와 좋아요/싫어요 수 간의 상관 관계')
plt.xlabel('댓글 수')
plt.ylabel('수')
plt.legend()
st.pyplot(fig)

# 상관 계수 출력
st.header('상관 계수')
st.write(f'댓글 수와 좋아요 수의 상관 계수: {correlation_comments_likes:.2f}')
st.write(f'댓글 수와 싫어요 수의 상관 계수: {correlation_comments_dislikes:.2f}')
st.text("0.78의 양의 상관 계수는 댓글 수와 좋아요 수 간에 강한 양의 선형 관계")
st.text("댓글 수가 증가함에 따라 좋아요 수도 증가한다는 경향이 있다는 것을 의미")
st.text("동영상에 댓글이 많으면 좋아요도 증가할 가능성이 높습니다.")
st.text("0.58의 양의 상관 계수는 댓글 수와 싫어요 수 간에 강한 양의 선형 관계")
st.text("댓글 수가 증가함에 따라 싫어요 수도 증가한다는 경향이 있다는 것을 의미")
st.text("동영상에 댓글이 많으면 싫어요도 증가할 가능성이 높습니다.")
st.text("댓글 수가 증가하면 좋아요 및 싫어요 수도 증가할 가능성이 있다는 것을 시각적으로 확인할 수 있습니다.")

# 5. 조회수와 댓글 수 간의 상관 관계 분석
st.header("5. 조회수와 댓글 수 간의 상관 관계 (Matplotlib & Seaborn)")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='view_count', y='comment_count', hue='categoryId', palette='Set2')
plt.title('조회수와 댓글 수 간의 상관 관계')
plt.xlabel('조회수')
plt.ylabel('댓글 수')
st.pyplot(plt)
st.text("조회수가 증가하면 댓글 수도 증가하는 경향이 있습니다.")
