"""
#Exercicio 18: Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos
"""
volume = float(input('Informe um volume em metros cúbicos:'))
conversao = 1000 * volume

print(f'Esse volume em litros é = {conversao}')
