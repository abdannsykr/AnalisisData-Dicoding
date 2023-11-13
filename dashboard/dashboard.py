import streamlit as st
import pandas as pd

day = 'day.csv'
hour = 'hour.csv'

data_day = pd.read_csv(day)
data_hour = pd.read_csv(hour)

st.title('Dashboard Penyewaan Sepeda')

st.subheader('Dataset Per Hari')
st.write(data_day.head())

st.subheader('Histogram Jumlah Penyewaan per Hari')
st.bar_chart(data_day['cnt'])

st.subheader('Dataset Per Bulan')
st.write(data_hour.head())

st.subheader('Histogram Jumlah Penyewaan per Bulan')
st.bar_chart(data_hour.groupby('mnth')['cnt'].sum())
