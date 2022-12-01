"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do
salário imprima: Emprestimo não concedido, caso contrário imprima: Empréstimo concedido.
"""
salario = float(input('Dígite o seu salário:R$'))
prestacao = float(input('Informe o valor da prestação:R$'))

if (salario * 20/100) < prestacao:
    print('Espréstimo não concedido.')
else:
    print('Empréstimo concedido.')
