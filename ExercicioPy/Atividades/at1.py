#Atividade 1

a = int(input('Digite o valor de a: '))
b = int(input('Digite o vlor de b: '))
c = int(input('Digite o valor de c: '))
#bin cast isNumeric

total = a + b + c
print(f'A soma dos três valores é de: {total}')

#Atividade 2

frase = input('Digite uma frase: ')

fraseInvertida = frase[::-1]

if frase == fraseInvertida:
    print(fraseInvertida)
    print(True)
else:
    print('false')