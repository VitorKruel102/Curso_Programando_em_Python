"""
#Exercicio 26: Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M*0.0001, sendo M a área em metros quadrados e A a área em acres.
"""
area = float(input('Informe um valor de área em metros quadrados m²:'))
conversao = area * 0.0001

print(f'Essa área convertida em hectares, é = {conversao}')
