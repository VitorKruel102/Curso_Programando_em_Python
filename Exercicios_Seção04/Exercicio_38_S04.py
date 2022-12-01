"""
#Exercicio 38: Leia o sálario de um funcionario. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um
aumento de 25%
"""
salario = float(input('Informe o seu salário: R$'))
aumento = salario + (salario * 25 / 100)

print(f'O reajuste do seu salário foi para: R${aumento}')
