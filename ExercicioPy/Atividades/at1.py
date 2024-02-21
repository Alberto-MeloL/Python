# #Atividade 1
#so printa texto
# a = int(input('Digite o valor de a: '))
# b = int(input('Digite o vlor de b: '))
# c = int(input('Digite o valor de c: '))
# #bin cast isNumeric

# total = a + b + c
# print(f'A soma dos três valores é de: {total}')

#Atividade 2
#condicioais(tomada de decisão)
#for quando se sabe o fim
#while quando não se sabe o fim
#foreach(percorrer a lista)

# frase = input('Digite uma frase: ')

# fraseInvertida = frase[::-1]

# if frase == fraseInvertida:
#     print(fraseInvertida)
#     print(True)
# else:
#     print('false')
    
idade = int(input('Sua idade: '))
    
while idade <18:
        for idade in range(18):
            print(idade)
            idade += 1
            print('')