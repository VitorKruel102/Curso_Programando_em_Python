"""
Exercicio 07: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula
de conversão é C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a tempreratura em Fahrenheit.
"""

temperatura = float(input('Dígite a temperatura em graus Fahrenheit:'))
celsius = 5.0 * (temperatura - 32.0) / 9.0

print(f'A sua temperatura em Celsius é: {celsius}')
