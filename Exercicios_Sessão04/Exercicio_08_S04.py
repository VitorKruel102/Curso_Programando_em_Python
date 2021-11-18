"""
#Exercicio 08: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula \
de conversão é C = k - 273.15, sendo C a temperatura em Celsius e k a tempreratura em Fahrenheit.
"""

temperatura = float(input('Dígite a temperatura em graus Kelvin:'))
celsius = temperatura - 273.15

print(f'A sua temperatura em Celsius é {celsius}')
