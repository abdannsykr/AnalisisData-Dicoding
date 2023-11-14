import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

day_file = 'day.csv'
hour_file = 'hour.csv'

data_day = pd.read_csv(day_file)
data_hour = pd.read_csv(hour_file)

st.title('Dashboard Penyewaan Sepeda')

st.subheader('Histogram Jumlah Penyewaan per Hari')
fig_day, ax_day = plt.subplots()
ax_day.bar(data_day.index, data_day['cnt'])
ax_day.set_xlabel('Tanggal')
ax_day.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig_day)

st.subheader('Histogram Jumlah Penyewaan per Bulan')
fig_hour, ax_hour = plt.subplots()
ax_hour.bar(data_hour.groupby('mnth')['cnt'].sum().index, data_hour.groupby('mnth')['cnt'].sum())
ax_hour.set_xlabel('Bulan')
ax_hour.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig_hour)
