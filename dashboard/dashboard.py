import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'weekday': ['jum/at', 'kamis', 'minggu', 'rabu', 'sabtu', 'selasa', 'senin'],
    'cnt': [4690.29, 4667.26, 4228.83, 4548.54, 4550.54, 4510.66, 4338.12]
})

st.title('Dashboard Penyewaan Sepeda')

st.write('Data Penyewaan Sepeda per Hari:')
st.dataframe(data)

st.bar_chart(data.set_index('weekday'))

data_bulan = pd.DataFrame({
    'mnth': ['Agustus', 'April', 'Desember', 'Februari', 'Januari', 'Juli', 'Juni', 'Maret', 'Mei', 'November', 'Oktober', 'September'],
    'cnt': [351194, 269094, 211036, 151352, 134933, 344948, 346342, 228920, 331686, 254831, 322352, 345991]
})

st.write('Data Penyewaan Sepeda per Bulan:')
st.dataframe(data_bulan)

st.bar_chart(data_bulan.set_index('mnth'))

