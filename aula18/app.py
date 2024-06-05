###_A PASTA TEM QUE SE CHAMAR TEMPLATES_###
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

###_Função para  análise de dados_###
def analise_dados(file_path):
    #carregar dados do arquivo csv
    df = pd.read_csv(file_path)

    fig1 = px.histogram(df, x=df.columns[-2], title='Distribuição de gráficos')
    fig1.write_html('templates/plot.html')

    #realizar um resumo sobre os dados
    resumo = df.describe()
    header = df.head()

    #retorno do resumo e do header
    return resumo, header

###_Flask seteup_###

app = Flask(__name__)

@app.route('/')
def index():
    #análisa os dados e gera os gráficos necessários
    resumo, header = analise_dados('movies.csv')

#onde vou renderizar
    return render_template('index.html', resumo=resumo.to_html(),
                            header=header.to_html())
@app.route('/plot')
def plot():
    render_template('templates/plot.html')

if __name__ == '__main__':
    app.run(debug=True)

###

