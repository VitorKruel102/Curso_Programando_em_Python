"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi
lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""
numero_recebido = 0
contador = 0
lista = []

while contador != 6:
    try:
        while contador != 6:
            numero_recebido = int(input('Digite um número:'))
            contador = contador + 1
            lista.append(numero_recebido)
        print(lista)
        minimo = min(lista)
        maximo = max(lista)
        print(f'O maior número digitado foi:{maximo} \nVocê repetiu o {maximo}:{lista.count(maximo)} vezes'
              f'\nO menor número digitado foi:{minimo}')
    except ValueError:
        print('Dado invalidos...')
