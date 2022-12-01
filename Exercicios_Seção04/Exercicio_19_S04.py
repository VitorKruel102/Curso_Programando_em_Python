"""
#Exercicio 19: Leia um valor de volume em litros  m³ e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos
"""
cubicos = float(input('Informe um volume em metros cúbicos:'))
conversao = cubicos / 1000

print(f'Esse volume em litros é = {conversao}³')
