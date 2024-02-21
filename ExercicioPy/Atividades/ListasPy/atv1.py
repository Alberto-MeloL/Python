#atividade 1
print('Atividae 1:')
numeros = [1, 2, 3, 4, 5]

for item in numeros:
    print(item)
    
#ativadade 2
print('Atividae 2:')
numerosReais = [-1, -2, 3, 7, 0, -7]

print(sorted(numerosReais))

#atividade 3
print('Atividae 3:')

notas = []

contador = 0

while contador < 4:
    try:
        notasLancadas = float(input('Digite as notas das quatro atividade do aluno:'))
        notas.append(notasLancadas)
        contador += 1 #incrementado em Python
    except ValueError:
        print('Digite apenas números', notas)
    
    if(len(notas) == 4):
            somaTotal = sum(notas)
            
            media = somaTotal / 4
            aprovado = 'Aprovado' if media >= 7 else 'Reprovado' 
            
            print(f'A média do aluno é: {media} o aluna está {aprovado}')
            
#atividade 4

letras = []

contador2 = 0

while contador2 < 10:
    try:
        letrasDigitadas = (input('Digite dez letas: '))
        letras.append(letrasDigitadas)
        contador2 += 1
        print(contador2)
        
    except ValueError:
        print('Digite apenas letras.')
        
        if contador2 == 10:
            print(type(letras))