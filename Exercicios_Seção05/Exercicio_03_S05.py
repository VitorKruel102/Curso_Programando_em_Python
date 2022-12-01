# Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado

number = float(input('Informe qualquer número real:'))

if number > 0:
    number = number ** 1/2
    print(f'A raiz quadrada do número é {number}')
else:
    number = number ** 2
    print(f'O número elevado á 2 é {number}')
