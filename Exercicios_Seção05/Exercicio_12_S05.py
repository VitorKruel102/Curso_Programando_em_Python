"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número invalido". Se o número for positivo,
calcular o logaritmo deste número.
"""

import math

number = float(input('Informe um número:'))

if number > 0:
    print(math.log(number))
else:
    print('Número invalido...')
