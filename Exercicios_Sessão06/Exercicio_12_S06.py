"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
decrescente.
"""
numero_recebido = ''

while numero_recebido != 'exit':
    numero_recebido = input('Digite um número inteiro positivo ou digite (exit) para sair:')
    if numero_recebido != 'exit':
        try:
            numero_recebido = int(numero_recebido)
            if numero_recebido > 0:
                for ordem_descrescente in range(numero_recebido, -1, -1):
                    print(ordem_descrescente, end=' ')
                break
            else:
                print('Dados invalidos...')
        except ValueError:
            print('Dado invalido...')
