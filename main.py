import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st


chart_data = pd.DataFrame(np.random.randn(500,5),columns=['a','b',
'c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b',
'c','d','e'])
st.altair_chart(chart)

df = pd.read_csv("Unemployment in India (1).csv")
col_list = df.columns.tolist()
choices = st.multiselect('What do you want to see?',col_list)
new_df = df[choices]
st.line_chart(new_df)
st.area_chart(new_df)


df = pd.read_csv("Unemployment in India (1).csv")
fig = px.pie(df,values=' Estimated Employed',names="Region",
opacity=0.7, color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

d1 = np.random.randn(200)
d2 = np.random.randn(200)
d3 = np.random.randn(200)

hist_data = [d1,d2,d3]
groups = ['G1','G2','G3']
fig = ff.create_distplot(hist_data,groups,bin_size=[.1,.25,.5])
st.plotly_chart(fig)