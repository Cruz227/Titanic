import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Titanic")
st.header("Read Titanic Dataset")
df = pd.read_csv("titanic.csv")
st.write("## DataFrame")
st.dataframe(df)
st.subheader("Información basica")
col1, col2, col3 = st.columns(3)
col1.metric("Filas", df.shape[0])
col2.metric("Columnas", df.shape[1])
col3.metric("valores nulos", df.isnull().sum().sum())
st.write("### Estadísticas ")
st.write(df.shape)
st.write(df.describe())

st.subheader("Visualización de datos")
with st.expander("Ver gráfico de barras de edades"):
    fig, ax = plt.subplots()
    sns.histplot(df['Age'].dropna(), bins=30, kde=True, ax=ax)
    ax.set_title("Distribución de Edades")
    st.pyplot(fig)





