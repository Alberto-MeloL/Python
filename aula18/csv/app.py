import streamlit as st 

import pandas as pd

df = pd.read_csv('movies.csv')

st.write(df.head())

filtro = st.sidebar.selectbox('Selecione o filtro',df.columns)
valor = st.sidebar.text_input('Digite o valor a ser filtrado:')

df_filtrado = df[df[filtro] == valor]

st.write(df_filtrado)