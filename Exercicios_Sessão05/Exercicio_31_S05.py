"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra qual a
classificação dessa pessoa.
//////////////////////          P E S O S         ////////////////////////////
                        ATÉ 60   60-90  ACIMA de 90
    - Menor que 1.20      A        D        G
    -  1.20 / 1.70        B        E        H
    - Maior que 1.70      C        F        I
"""
altura = float(input('Informe sua altura:'))
peso = float(input('Informe seu peso:'))

if altura < 1.20:
    if peso <= 60:
        print('Clasificação A')
    elif 60 < peso <= 90:
        print('Clasificação D')
    else:
        print('Classificação G')
elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        print('Clasificação B')
    elif 60 < peso <= 90:
        print('Clasificação E')
    else:
        print('Classificação H')
elif altura > 1.70:
    if peso <= 60:
        print('Clasificação C')
    elif 60 < peso <= 90:
        print('Clasificação F')
    else:
        print('Classificação I')
else:
    print('Dados invalidos...')
