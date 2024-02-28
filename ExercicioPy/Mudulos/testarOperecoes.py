import operacoes

a:int = 10
b:int = 10

print(operacoes.somar(a,b))
print(operacoes.subtrair(a, b))

dados = [2, 3, 5, 7, 11, 13, 17]
media = operacoes.calcular_media(dados)
mediana = operacoes.calcular_mediana(dados)

print(media)
print(mediana)
