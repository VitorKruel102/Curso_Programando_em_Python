"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas(as básicas, por exemplo). O
Usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostre o
resultado e saindo.
"""
operacao = str(input('Informe qual operação matemática: \n(+) \n(-) \n(/) \n(*) \nQual operação:'))
dado01 = float(input('Informe um número:'))
dado02 = float(input('Informe outro número:'))

if operacao == '+':
    soma = dado01 + dado02
    print(f'A soma é:{soma}')
elif operacao == '-':
    menos = dado02 - dado01
    print(f'A subtração é:{menos}')
elif operacao == '*':
    vezes = dado01 * dado02
    print(f'A multiplicação é:{vezes}')
elif operacao == '/':
    div = dado01 / dado02
    print(f'A divisão é:{div}')
else:
    print('Operação invalida')
