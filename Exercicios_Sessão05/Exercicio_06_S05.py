"""
Escrea um programa que, dados dois números inteiros, mostre na tela o maior deles, assim com a diferença existente
entre ambos.
"""
number01 = float(input('Informe o primeiro número:'))
number02 = float(input('Informe o segundo número:'))

if number01 > number02:
    print(f'O maior número é:{number01} \nE a diferença é:{number01 - number02}')
elif number01 == number02:
    print('Os números são iguis.')
else:
    print(f'O maior número é:{number02} \nE a diferença é:{number02 - number01}')
