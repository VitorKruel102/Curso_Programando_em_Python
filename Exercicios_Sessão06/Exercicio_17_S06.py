# Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros números natuais.
numero_recebido = ''

while numero_recebido != 'exit':
    numero_recebido = input('Digite um número inteiro positivo ou digite (exit) para sair:')
    if numero_recebido != 'exit':
        try:
            numero_recebido = int(numero_recebido)
            if numero_recebido > 0:
                numeros = 0
                for primeiros_numeros in range(0, numero_recebido + 1):
                    numeros += primeiros_numeros
                print(f'A soma dos primeiros {numero_recebido} numeros naturais é = {numeros}')
                break
            else:
                print('Dados invalidos...')
        except ValueError:
            print('Dados invalidos...')
