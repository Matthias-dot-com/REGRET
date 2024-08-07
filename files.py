import streamlit as st
import pandas as pd

st.subheader("Loading Files")

data = st.file_uploader("Upload Your CSV or excel file here : ",type=['csv','xlsx'])
if data is not None:
    file = pd.read_csv(data)
    st.table(file.head())
button = st.button('show full data')
if data is not None and button :
    st.table(file)
button=st.button('only first 5 elements')
if button:
    st.table(file.head())
data = pd.read_csv('Unemployment in India (1).csv')
st.table(data.head())

st.image(r"C:\Users\matth_ik1hap6\OneDrive\Pictures\Screenshots\Screenshot 2024-06-02 165552.png")
st.text('Wanna upload your own image :')
img = st.file_uploader("Upload Your Image here : ",type=['img','png','jpeg','jpng'])
st.image(img)
video = st.file_uploader("Upload Your Video here : ",type=['mp4'])
audio = st.file_uploader("Upload Your audio here : ",type=['mp3','wav'])

