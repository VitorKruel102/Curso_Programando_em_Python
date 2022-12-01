# Faça um programa que peça ao usuário para digitar 10 valores e some-os.
soma_numeros = 0
numero_recebido = 0
contador = 0

while contador != 10:
    try:
        while contador != 10:
            numero_recebido = int(input('Digite um número:'))
            soma_numeros += numero_recebido
            contador = contador + 1
        print(f'A soma dos dados enviados é:{soma_numeros}')
    except ValueError:
        print('Dados invalidos...')
