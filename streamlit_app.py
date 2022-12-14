import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.write('Below is a dataframe:', df, 'Above is a dataframe')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

df2['c'] = df2['c'].apply(lambda x: -1*x*5)
st.write(df2.head())
st.caption('the head of the secod dataframe')
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)