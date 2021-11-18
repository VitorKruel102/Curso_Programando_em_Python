# Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímparares.
numero_recebido = ''
contador = 0
lista = []

while numero_recebido < "exit":
    numero_recebido = input('Digite um número inteiro ou digite (exit) para sair:')
    if numero_recebido != 'exit':
        try:
            numero_recebido = int(numero_recebido)
            for numero in range(1, numero_recebido):
                if numero % 2 != 0:
                    lista.append(numero)
            print(f'Os primeiros {numero_recebido} números impares são: {lista}')
            break
        except ValueError:
            print('Dados Invalidos...')
