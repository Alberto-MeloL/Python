
import pandas as pd
df_supermarket = pd.read_json('supermarket.json')

def extrair_dado_loja_mes(loja_id, mes):
    for loja in df_supermarket['lojas']:
        if loja['id'] == loja_id:
            for dados_mensais in loja['dados_mensais']:
                if dados_mensais['mes'] == mes:
                    return dados_mensais
    return None

extrair_dado_loja_mes(5,8)

# função para retornar o faturamento do mes

def faturamento_mensal(loja_id, mes):
    for loja in df_supermarket['lojas']:
        if loja['id'] == loja_id:
            for dados_mensais in loja['dados_mensais']:
                if dados_mensais['mes'] == mes:
                    for faturamento in dados_mensais['faturamento']:
                        faturamento = sum(dados_mensais['faturamento'])
                    return faturamento
                return None
            faturamento_mensal(8,5)

def extrair_faturamento_loja_ano(loja_id):
    for loja in df_supermarket['lojas']:
        if loja['id'] == loja_id:
            for dados_mensais in loja['dados_mensais']:
                if dados_mensais['mes'] == loja_id:
                    for faturamento in dados_mensais['faturamento']:
                        faturamento = sum(dados_mensais['faturamento'])
                    return faturamento
                return None
            faturamento_mensal(8,5)

def faturamento_mensal(loja_id, mes):
    for loja in df_supermarket['lojas']:
        if loja['id'] == loja_id:
            for dados_mensais in loja['dados_mensais']:
                if dados_mensais['mes'] == mes:
                    for faturamento in dados_mensais['faturamento']:
                        faturamento = sum(dados_mensais['faturamento'])
                    return faturamento
                return None
            faturamento_mensal(8,5)
