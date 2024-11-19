import streamlit as st 
import pandas as pandas

st.title("Website Deverloper Profesional Python")
st.header("Website Deverloper Profesional Python")

st.image('./img/kairung.jpg')
st.subheader("Pattanapong Sukhamsaen")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))