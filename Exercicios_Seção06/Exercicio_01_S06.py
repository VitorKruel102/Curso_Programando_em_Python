# Faça um programa que determine e mostre os 5 primeiros múltiplos de 3, considerando números maiores que 0.
multiplo = 5
lista = []

for numero in range(1, multiplo + 1):
    lista.append(3 * numero)
print(lista)
