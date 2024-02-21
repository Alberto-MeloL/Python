#em python você pode misturar a lista, mas em outra linguagens pode ser uma péssima prática
#lista apenas de um tipo(String, Integer, etc...)

#Criação de Listas:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de strings
frutas = ["maçã", "banana", "laranja"]

# Lista mista
misturada = [1, "python", True, 3.14]

#Acesso a Elementos:

# Acesso por índice
primeiro_elemento = numeros[0]  # Resultado: 1

# Índices negativos contam a partir do final
ultimo_elemento = frutas[-1]  # Resultado: "laranja"


#Modificação de Elementos:

# Modificar um elemento
frutas[1] = "kiwi"  # Agora a lista é ["maçã", "kiwi", "laranja"]

#Adição e Remoção de Elementos:

# Adicionar elemento ao final da lista
frutas.append("uva")  # Resultado: ["maçã", "kiwi", "laranja", "uva"]

# Remover elemento por valor
frutas.remove("kiwi")  # Resultado: ["maçã", "laranja", "uva"]

#operações e métodos úteis:
#len(): retorna o número de elementos na lista
#append(): adiciona um elemento ao final da lista
#pop(): remove e retornq o último elemento da lista
#insert(): insere um elemento em uma posição específica
#remove(): remove o primeiro elemento com um valor específico
#Slicing: permite criar sublistas usando a notação de slicing

#o que tem indíce:
#lista e tuplas

#o que não tem indíce:
#diciomário e conjunto  