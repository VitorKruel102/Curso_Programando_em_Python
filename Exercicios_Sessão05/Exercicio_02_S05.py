"""
Leia um número fornecido pelo usuáio. Se esse número for positivo, calcule a raiz quadrada do número do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.
"""
number = float(input('Informe qualquer número:'))

if number >= 0:
    number = number ** 1/2
    print(f'A raiz quadrada é {number}')
else:
    print('Número infalido')
