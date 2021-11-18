"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverpa ser informado o número de dados
lidos e números de valores pares. O processo termina quando for digitado o número 1000.
"""
lista_pares = []
numero_recebido = 0
contador = 0

while contador < 6:
    try:
        numero_recebido = int(input('Digite um número:'))
        if numero_recebido != 1000:
            contador = contador + 1
            if numero_recebido % 2 == 0:
                lista_pares.append(numero_recebido)
        else:
            break
    except ValueError:
        print('Dados invalidos...')
print(f'{contador} números foram lidos \nE os números pares dessa lista são:{lista_pares}')
