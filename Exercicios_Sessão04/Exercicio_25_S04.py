"""
#Exercicio 25: Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.
"""
area = float(input('Informe um valor de área em acres:'))
conversao = area * 4048.58

print(f'Essa área convertida em metros quadrados, é = {conversao}²')
