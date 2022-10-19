"""
===============================================

        Try, Except, Else e Finally

===============================================
"""
try:
    numero = int(input('Informe um número: '))
except ValueError as Erro_valor:
    print(f'Valor incorreto')
else:
    print(f'Você digitou {numero}')
finally:
    print('Finalização...')

def dividir(a, b):
    """."""
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Precisa ser um número númericico'
    except ZeroDivisionError:
        return 'Não podemos dividir por 0'

numero_01 = input('Numero 01: ')
numero_02 = input('Numero 02: ')
print(dividir(numero_01, numero_02))
