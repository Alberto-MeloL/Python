import streamlit as st
import pandas as pd 

st.title('Minha primeira aplicação')

st.header('Cabeçalho secundário')

st.subheader('Cabeçalho terciário')

st.text('Deus é poderoso!')

st.markdown('**Este é um texto em negrito usando Markdown.**')

st.sidebar.title('Barra lateral')

st.sidebar.markdown('Texto simples')

col1, col2 = st.columns(2)

col1.write('Coluna 1')
col2.write('Coluna 2')

if col1.button('Clique aqui'):
    col1.write('Botão clicado!')
else:
    col1.write('')

if col2.checkbox('Marque-me'):
    col2.write('Caixa marcada!')


# identação para não ficar dentro do bloco if
age = col2.slider('Selecione a sua idade:', 0,100,1)
col1.write(f'Sua idade é: {age}')

nome = col2.text_input('Digite seu nome')
col2.write(f'Seu nome é: {nome}')

data = {'Coluna 1': [1,2,3], 'Coluna 2': [4,5,6]}

df = pd.DataFrame(data)

st.write(df)

col2.table(df)