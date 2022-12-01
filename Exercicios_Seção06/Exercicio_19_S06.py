"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o
número:
"""
numero_recebido = 0

while numero_recebido != 1:
    try:
        numero_recebido = int(input('Digite um número entre 100 a 999 ou digite (1) para sair:'))
        if numero_recebido != 1:
            if 100 <= numero_recebido <= 999:
                separacao = str(numero_recebido)
                print(f'{separacao[0]} \n{separacao[1]} \n{separacao[2]}')
            else:
                print('Dados invalidos...')
    except ValueError:
        print('Dados invalidos...')
