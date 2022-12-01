# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
numeros_recebidos = 0
soma_numeros = 0
media_numeros = 0
dados_validos = 0
contador = 0

while contador != 10:
    try:
        while contador != 10:
            numeros_recebidos = int(input('Digite um número:'))
            contador = contador + 1
            if numeros_recebidos >= 0:
                soma_numeros += numeros_recebidos
                dados_validos += (numeros_recebidos - numeros_recebidos) + 1
                media_numeros = soma_numeros / dados_validos
        print(f'a média dos números informados positivos informados é:{media_numeros}')
    except ValueError:
        print('Dados invalidos')
