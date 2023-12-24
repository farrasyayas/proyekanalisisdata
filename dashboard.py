import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df1 = pd.read_csv('day.csv')
df2 = pd.read_csv('hour.csv')

# Cleaning Data - Daily Data (df1)
df1.dropna(inplace=True)
df1['dteday'] = pd.to_datetime(df1['dteday'])
df1.drop_duplicates(inplace=True)

# Cleaning Data - Hourly Data (df2)
df2.dropna(inplace=True)
df2['dteday'] = pd.to_datetime(df2['dteday'])
df2.drop_duplicates(inplace=True)

# Streamlit App
st.title("Analisis Data Rental Sepeda")

# Sidebar
st.sidebar.subheader("Pilih Visualisasi!")

# Assessing Data - Daily Data (df1)
if st.sidebar.checkbox("Show Data - Daily Data (df1)"):
    st.subheader("Daily Data (df1)")
    st.write(df1)

if st.sidebar.checkbox("Summary Statistics - Daily Data (df1)"):
    st.subheader("Summary Statistics - Daily Data (df1)")
    st.write(df1.describe())

# Assessing Data - Hourly Data (df2)
if st.sidebar.checkbox("Show Data - Hourly Data (df2)"):
    st.subheader("Hourly Data (df2)")
    st.write(df2)

if st.sidebar.checkbox("Summary Statistics - Hourly Data (df2)"):
    st.subheader("Summary Statistics - Hourly Data (df2)")
    st.write(df2.describe())

# EDA - Daily Data (df1)
if st.sidebar.checkbox("Histogram - Rental Sepeda Harian"):
    st.subheader("Histogram - Rental Sepeda Harian")
    plt.figure(figsize=(10, 6))
    sns.histplot(df1['cnt'], bins=30, kde=True)
    plt.title('Distribusi Rental Sepeda Harian')
    plt.xlabel('Jumlah Rental Sepeda')
    plt.ylabel('Frekuensi')
    st.pyplot()

if st.sidebar.checkbox("Matriks Korelasi - Rental Sepeda Harian"):
    st.subheader("Matriks Korelasi - Rental Sepeda Harian")
    plt.figure(figsize=(12, 8))
    corr_matrix = df1.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriks Korelasi - Rental Sepeda Harian')
    st.pyplot()

if st.sidebar.checkbox("Time Series - Rental Sepeda Harian"):
    st.subheader("Time Series - Rental Sepeda Harian")
    plt.figure(figsize=(14, 6))
    plt.plot(df1['dteday'], df1['cnt'], label='Rental Sepeda', color='blue')
    plt.title('Rental Sepeda Harian Sepanjang Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Rental Sepeda')
    plt.legend()
    st.pyplot()

# EDA - Hourly Data (df2)
if st.sidebar.checkbox("Histogram - Rental Sepeda Berdasarkan Jam"):
    st.subheader("Histogram - Rental Sepeda Berdasarkan Jam")
    plt.figure(figsize=(10, 6))
    sns.histplot(df2['cnt'], bins=30, kde=True)
    plt.title('Distribusi Rental Sepeda Berdasarkan Jam')
    plt.xlabel('Jumlah Rental Sepeda')
    plt.ylabel('Frekuensi')
    st.pyplot()

if st.sidebar.checkbox("Matriks Korelasi - Rental Sepeda Berdasarkan Jam"):
    st.subheader("Matriks Korelasi - Rental Sepeda Berdasarkan Jam")
    plt.figure(figsize=(12, 8))
    corr_matrix_hourly = df2.corr()
    sns.heatmap(corr_matrix_hourly, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriks Korelasi - Rental Sepeda Berdasarkan Jam')
    st.pyplot()

if st.sidebar.checkbox("Time Series - Rental Sepeda Berdasarkan Jam"):
    st.subheader("Time Series - Rental Sepeda Berdasarkan Jam")
    plt.figure(figsize=(14, 6))
    plt.plot(df2['dteday'], df2['cnt'], label='Rental Sepeda', color='green')
    plt.title('Rental Sepeda Berdasarkan Jam Sepanjang Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Rental Sepeda')
    plt.legend()
    st.pyplot()

# Visualisasi untuk Pertanyaan 1 - Pengaruh Cuaca dan Tren Musiman pada Peminjaman Sepeda Harian (df1)
if st.sidebar.checkbox("Pengaruh Cuaca dan Tren Musiman pada Rental Sepeda Harian"):
    st.subheader("Pengaruh Cuaca dan Tren Musiman pada Rental Sepeda Harian")
    plt.figure(figsize=(14, 8))
    sns.lineplot(x='mnth', y='cnt', data=df1, hue='weathersit', marker='o', ci=None)
    plt.title('Pengaruh Cuaca dan Tren Musiman pada Rental Sepeda Harian')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Rental Sepeda')
    st.pyplot()

# Visualisasi untuk Pertanyaan 2 - Pengaruh Cuaca dan Jam pada Peminjaman Sepeda per Jam (df2)
if st.sidebar.checkbox("Pengaruh Cuaca dan Jam pada Rental Sepeda per Jam"):
    st.subheader("Pengaruh Cuaca dan Jam pada Rental Sepeda per Jam")
    plt.figure(figsize=(16, 8))
    sns.pointplot(x='hr', y='cnt', data=df2, hue='weathersit', dodge=True, markers='o', linestyles='-', errwidth=1)
    plt.title('Pengaruh Cuaca dan Jam pada Rental Sepeda per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Rental Sepeda')
    st.pyplot()
    
st.set_option('deprecation.showPyplotGlobalUse', False)
