"""
Escreva um programa que leia um número inteiro maior do que zero a devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8(2+5+1). Se o número lido não for maior do que zero, o programa
terminará com mensagem"Número invalido".
"""

number = int(input('Digite um número maior que zero até 4 digitos:'))

if int(number) > 0 and (number < 10000):
    u = number // 1 % 10
    d = number // 10 % 10
    c = number // 100 % 10
    m = number // 1000 % 10
    soma = u + d + c + m
    print(f'Soma de todos os algarismos é:{soma}')
else:
    print('Número é invalido')


