# Escreva um programa que leia 10 números e escreva o menor valor lido e o menor valor lido.
numero_recebido = 0
lista = []
contador = 0

while contador < 10:
    try:
        while contador < 10:
            numero_recebido = int(input('Digite um número:'))
            lista.append(numero_recebido)
            contador = contador + 1
        print(lista)
        menor_numero = min(lista)
        maior_numero = max(lista)
        print(f'O maior número digitado é:{maior_numero} \nO menor número digitado é:{menor_numero}')
    except ValueError:
        print('Dado invalido')
