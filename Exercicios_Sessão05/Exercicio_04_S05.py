"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado;
    - A raiz quadrada do número digitado;
"""

number = float(input('Digite um número:'))

if number > 0:
    number01 = number ** 2
    number02 = number ** 1/2
    print(f'O {number}² = {number01} \nA raiz quadrada de {number} = {number02}')
else:
    print('Número invalido, tente outro...')
