"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com
um valor numérico digitado pelo usuário:
    (a) - Geométrica= 3RAIZ(x*y*z)
    (b) Ponderada = (x+2*y+3*z) / 6
    (c) Harmônia = 1 / (1/x + 1/y + 1/z)
    (d) Aritmédica = (x+y+z) / 3
"""
x = int(input('Informe o núemro de x:'))
y = int(input('Informe o núemro de y:'))
z = int(input('Informe o núemro de z:'))

opcao = str(input('Escolha a operção matematíca: \na - Geométrica \nb - Ponderada \nc - Harmônia \nd - Aritmédica \n'
                  ' Informe a letra correspondente a operação:'))

if opcao.upper() == 'A':
    geometrica = (x * y * z) ** 1 / 3
    print(f'O resultado é:{geometrica}')
elif opcao.upper() == 'B':
    ponderada = (x + (2 * y) + (3 * z)) / 6
    print(f'O resultado é:{ponderada}')
elif opcao.upper() == 'C':
    harmonia = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f'O resultado é:{harmonia}')
elif opcao.upper() == 'D':
    aritmeica = (x + y + z) / 3
    print(f'O resultado é:{aritmeica}')
else:
    print('Dados não são validos...')
