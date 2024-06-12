import streamlit as st

st.title('Calculadora Básica')
col1, col2 = st.columns(2)
operacoes = col1.selectbox('Selecione a opereção',('+', '-', '*', '/', '**'))

n1:int = col2.number_input('Digite o primeiro número:')
n2:int = col2.number_input('Digite o segundo número:')


if operacoes == '+':
    col1.write(n1 + n2)

if operacoes == '-':
    col1.write(n1 - n2)

if operacoes == '*':
    col1.write(n1 * n2)

if operacoes == '/':
    col1.write(n1 / n2)

    # pão de mel