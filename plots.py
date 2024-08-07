import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.subheader("Plots")

df = pd.DataFrame(np.random.randn(20,3),columns=["A","B","C"])
img = plt.plot(df["A"],df["B"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# st.table(df)
df = pd.read_csv('Unemployment in India (1).csv')
st.dataframe(df)
# print(df.columns)
fig = plt.figure(figsize=(15,5))
df["Region"].value_counts().plot(kind="bar")
st.pyplot(fig)

fig = plt.figure(figsize=(15,5))
sns.distplot(df[" Estimated Employed"])
st.pyplot(fig)


col1,col2 = st.columns(2)

with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df[" Estimated Employed"],kde = False)
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure()
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df[" Estimated Unemployment Rate (%)"],hist = False)
    st.pyplot(fig2)


fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)


fig = plt.figure(figsize=(15,5))
sns.countplot(df,x="Region")
st.pyplot(fig)


fig = plt.figure(figsize=(15,5))
sns.boxplot(df,x="Region",y=" Estimated Employed")
st.pyplot(fig)

fig = plt.figure(figsize=(15,5))
sns.violinplot(df,x="Region",y=" Estimated Employed")
st.pyplot(fig)

