"""
#Exercicio 42: Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse
funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
"""
salario_base = float(input('Informe o seu salário-base:R$'))
imposto = salario_base - (salario_base * 7 / 100)
receber = imposto + (salario_base * 5 / 100)

print(f'O seu salário liquido é:R${receber}')
