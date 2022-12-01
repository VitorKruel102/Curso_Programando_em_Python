# Faça um programa que receba três números e mostre-os em ordem crescente.

number1 = float(input('Digite o primeiro número:'))
number2 = float(input('Digite o segundo número:'))
number3 = float(input('Digite o terceiro número:'))

lista = [number1, number2, number3]
lista.sort()
x = lista.pop()
y = lista.pop()
z = lista.pop()

print(f'A ordem crescente dessa sequência é: \n{z} \n{y} \n{x}')
