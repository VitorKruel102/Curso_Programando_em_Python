"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de
repetição 'for', a segunda 'while', e a terceira 'do while'.
"""

for numero in range(1, 11, 1):
    print(numero)
numero = 1
while numero < 11:
    print(numero)
    numero = numero + 1
numero = True
while numero:
    for numero in range(1, 11, 1):
        print(numero)
        numero = False
