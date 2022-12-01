"""
#Exercicio 41: Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pagos ao funcionário, adicionanado 10% sobre o valor calculado.
"""
valor = float(input('Informe o valor da hora trabalhadas:R$'))
hora = float(input('Informe a carga horária do mês:'))
total = (valor * hora) + ((valor * hora) * 10 / 100)

print(f'O valor a ser pago é: R${total}')
