"""
Exercicio 06: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A formula
de conversão é F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a tempreratura em Celsius.
"""

temperatura = float(input('Dígite a temperatura em graus Celsius:'))
fahrenheit = temperatura * (9.0/5.0) + 32.0

print(f'A sua temperatura em Fahrenheit é: {fahrenheit}')
