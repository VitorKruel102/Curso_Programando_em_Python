"""
#Exercicio 27: Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
"""
area = float(input('Informe o valor da área em hectar:'))
conversao = area * 10000

print(f'A conversão da área para metros quadrados é: {conversao}²')
