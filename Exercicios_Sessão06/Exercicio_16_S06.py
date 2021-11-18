"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números naturais de 0 até N em ordem
decrescente.
"""
numero_recebido = ''

while numero_recebido != 'exit':
    numero_recebido = input('Digite um número inteiro positivo impar ou digite (exit) para sair:')
    if numero_recebido != 'exit':
        try:
            numero_recebido = int(numero_recebido)
            if numero_recebido > 0:
                if numero_recebido % 2 != 0:
                    for ordem_decrescente in range(numero_recebido, -1, -1):
                        if ordem_decrescente % 2 != 0:
                            print(ordem_decrescente, end=' ')
                    break
                else:
                    print('Dados invalidos...')
            else:
                print('Dados invalidos...')
        except ValueError:
            print('Dados invalidos...')
