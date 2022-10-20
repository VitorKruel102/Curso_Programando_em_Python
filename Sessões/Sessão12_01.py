"""
===============================================

                Modulos

===============================================
"""
from random import random, uniform, randint, choice, shuffle

jogadas = ['Pedra', 'papel', 'tesoura']
cartas  = ['K', 'Q', 'J', 'A', '2', '3', '4', '5']

shuffle(cartas)

print(random())
print(uniform(3, 7)) 
print(randint(3, 7))
print(choice(jogadas))
print(cartas) 

def range_aleatorio():
    """Retorna uma lista com 10 números aleatórios."""
    lista = []
    for i in range(10):
        lista.append(random())

    return lista

