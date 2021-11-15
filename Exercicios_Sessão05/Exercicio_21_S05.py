"""
Escreva o menu de opeções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro
se a opção for invalida.
Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 números (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
"""
opcao = str(input('Escolha a opção: \n1 - Soma de 2 número. \n2 - Diferença entre 2 números(maior pelo menor). \n3 -'
                  ' Produto entre 2 números. \n4 - Dívisão entre 2 números(o denominador não pode ser zero). \nQual'
                  ' o opção você escolhe:'))

if opcao == '4':
    dado00 = float(input('Informe um número:'))
    dado01 = float(input('Informe outro número porém não pode ser = 0 \nDigite o número:'))
    if dado01 != 0:
        div = dado00 / dado01
        print(f'A dívisão é:{div}')
    else:
        print('Número invalido')
else:
    if opcao == '1':
        dado00 = float(input('Informe um número:'))
        dado01 = float(input('Informe outro número:'))
        soma = dado00 + dado01
        print(f'A soma dos números é:{soma}')
    elif opcao == '2':
        dado00 = float(input('Informe um número:'))
        dado01 = float(input('Informe outro número:'))
        if dado00 > dado01:
            cal = dado00 - dado01
            print(f'A diferença entre eles é:{cal}')
        else:
            cal = dado01 - dado00
            print(f'A diferença entre eles é:{cal}')
    elif opcao == '3':
        dado00 = float(input('Informe um número:'))
        dado01 = float(input('Informe outro número:'))
        mul = dado00 * dado01
        print(f'O produto desses valores é:{mul}')
