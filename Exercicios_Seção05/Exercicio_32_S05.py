"""
Escreva um programa que leia o códico do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve
calcular o valor a ser pago por aquele lanche. Considere que a cada a execução somente será calculado um pedido. O
cardápio da lanchonete segue o padrão abaixo:
                        Códico   Preço
    - Cachorro Quente:   100     1.20
    - Bauru Simples:     101     1.30
    - Bauru com ovo:     102     1.50
    - Hamburger:         103     1.20
    - Cheeseburger:      104     1.70
    - Suco:              105     2.20
    - Refrigerante:      106     1.00
"""
print('Bem vindo(a) a Lanchonete da Marinha.')
print('Segue abaixo a lista do cardápio:')
print('100 - Cachorro Quente = R$1.20.')
print('101 - Bauru Simples =  R$1.30')
print('102 - Bauru com ovo = R$1.50')
print('103 - Hamburger = R$1.20')
print('104 - Cheeseburger = R$1.70')
print('105 - Suco = R$2.20')
print('106 - Refrigerante = R$1.00')

codico = int(input('Informe o códico do seu lanche:'))
quantidade = int(input('Qual a quantidade desejada:'))

if 100 <= codico <= 106:
    if codico == 100:
        print(f'O valor a ser pago: R${quantidade * 1.20}')
    elif codico == 101:
        print(f'O valor a ser pago: R${quantidade * 1.30}')
    elif codico == 102:
        print(f'O valor a ser pago: R${quantidade * 1.50}')
    elif codico == 103:
        print(f'O valor a ser pago: R${quantidade * 1.520}')
    elif codico == 104:
        print(f'O valor a ser pago: R${quantidade * 1.70}')
    elif codico == 105:
        print(f'O valor a ser pago: R${quantidade * 2.20}')
    elif codico == 106:
        print(f'O valor a ser pago: R${quantidade * 1.00}')
else:
    print('Códico invalido.')
