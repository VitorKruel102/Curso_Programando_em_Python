"""
#Exercicio 09: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A formula
de conversão é K = C + 273.15, sendo K a temperatura em Kelvin e C a tempreratura em Celsius.
"""
temperatura = float(input('Dígite a temperatura em graus Celsius:'))
kelvin = temperatura + 273.15

print(f'A sua temperatura em Kelvin é {kelvin}')
