import streamlit as st 
import pandas as pd

st.title("Website Deverloper Profesional Python")
st.header("Website Deverloper Profesional Python")

st.image('./img/1.jpg')
st.subheader("Pattanapong Sukhamsaen")

dt=pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))