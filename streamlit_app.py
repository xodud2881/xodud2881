import streamlit as st
from tkinter.tix import COLUMN
from pyparsing import empty
import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title('파이썬시각화 11조')

	
df = pd.read_csv('./경찰청_전국 범죄 발생 및 검거 현황_20211231.csv', encoding='cp949')
### 경로맞추셔서 저희 카톡방에 올라인 데이터 파일 read해주시면 되요


df['검거율'] = (df['검거'] / df['발생']) * 100 
df['남성 검거율'] = df['검거인원(남)'] / (df['검거인원(남)'] + df['검거인원(여)']) * 100
df['여성 검거율'] = df['검거인원(여)'] / (df['검거인원(남)'] + df['검거인원(여)']) * 100


g1,g2,g3 = st.columns(3)

with g1 :
    범죄대분류 = df['범죄대분류'].unique().tolist()

    my_choice = st.selectbox('범죄대분류 선택하기', 범죄대분류)


    df_second = df[df['범죄대분류'] == my_choice]
    

    범죄중분류 = df_second['범죄중분류'].unique().tolist()
    my_choice2 = st.selectbox('범죄중분류 선택하기', 범죄중분류)

    df_third = df_second[df_second['범죄중분류'] == my_choice2]
  

    fig = px.bar(df_third, x='범죄소분류', y='검거율',title= '선택 범죄분류별 검거율')
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)
	
	
with g2 :
  
  남자검거총합 = df_third['검거인원(남)'].sum()
  여자검거총합 = df_third['검거인원(여)'].sum()
  남자검거비율 = 남자검거총합 / (남자검거총합 + 여자검거총합) * 100
  여자검거비율 = 여자검거총합 / (남자검거총합 + 여자검거총합) * 100
  
  fig2 = go.Figure(data=go.Pie(labels=['남성 검거율','여성 검거율'], values = [남자검거비율,여자검거비율],title= '선택 범죄분류 남녀별 검거율'))
  fig2.update_layout(width=800, height=600)
  st.plotly_chart(fig2) 
    
with g3 :
  불상총합 = df_third['불상'].sum()
  df_forth = df_third
  df_forth['불상비율'] = (df_forth['불상'] / 불상총합) * 100
  
  
  fig3 = px.bar(df_forth, x='범죄소분류', y='불상비율',title= '선택 범죄분류별 불상비율')
  fig3.update_layout(width=800, height=600)
  st.plotly_chart(fig3)
