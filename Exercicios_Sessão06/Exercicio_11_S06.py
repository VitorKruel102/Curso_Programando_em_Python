"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
crescente.
"""
numero_recebido = ''

while numero_recebido != 'exit':
    numero_recebido = input('Digite um número inteiro ou digite (exit) para sair:')
    if numero_recebido != 'exit':
        try:
            numero_recebido = int(numero_recebido)
            if numero_recebido > 0:
                for ordem_crescente in range(0, numero_recebido + 1):
                    print(ordem_crescente, end=' ')
                break
            else:
                print('Dados invalidos...')
        except ValueError:
            print('Dado Invalido...')
