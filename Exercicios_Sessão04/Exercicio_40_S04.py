"""
#Exercicio 40: Uma empresa contrata um encanador a R$30.00 por dia. Faça um programa que solicite o número de dias
trabalhadas pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para
importo de renda.
"""
dias = int(input('Informe o número de dias trabalhados:'))
descontados = (30.00 * dias) - ((30.00 * dias) * 8 / 100)

print(f'O valor a receber líquido ficará R${descontados}, ja descontando os 8% do imposto de renda')
