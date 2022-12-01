# Faça um programa que leia 10 inteiros e imprima sua média.
soma_numeros = 0
numeros_recebidos = 0
media = 0
contador = 0

while contador != 10:
    try:
        while contador != 10:
            numeros_recebidos = int(input('Digite um número'))
            soma_numeros += numeros_recebidos
            media = soma_numeros / 10
            contador = contador + 1
        print(f'A média dos dados enviados é:{media}')
    except ValueError:
        print('Dado invalido...')
