# Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
numero_pares = 0
soma_numero_pares = 0
numero = 0

while numero_pares != 50:
    numero = numero + 1
    if numero % 2 == 0:
        soma_numero_pares += numero
        numero_pares += 1
print(f'A foma dos 50 primeiros números pares é = {soma_numero_pares}')
