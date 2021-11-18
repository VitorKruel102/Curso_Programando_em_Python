"""
#Exercicio 24: Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M*0.000247, sendo M a área em metros quadrados e A a área em acres.
"""
area = float(input('Informe um valor de área em metros quadradas em m²:'))
conversao = area * 0.000247

print(f'Essa área convertida em acres, é = {conversao}')
