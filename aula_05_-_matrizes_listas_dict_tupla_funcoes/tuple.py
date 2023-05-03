"""
tuple é uma forma imutável de lista
"""

# Criando uma tupla de frutas
frutas = ("maçã", "banana", "laranja", "abacaxi")

# Imprimindo a tupla na tela
print(frutas)

# Acessando um elemento específico da tupla
print(frutas[0])  # Imprime "maçã"

# Tentando alterar um elemento da tupla (o que não é permitido)
frutas[0] = "pêra"  # Gera um TypeError: 'tuple' object does not support item assignment


"""
Neste exemplo, criamos uma tupla chamada frutas, contendo quatro elementos: "maçã", "banana", "laranja" e "abacaxi". Depois, imprimimos a tupla na tela e acessamos o primeiro elemento usando seu índice (0). Note que, ao tentarmos alterar um elemento da tupla (atribuindo um novo valor a frutas[0]), ocorre um erro TypeError, pois tuplas são imutáveis em Python.
"""