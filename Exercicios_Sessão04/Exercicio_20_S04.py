"""
#Exercicio 20: Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
quilogramas = float(input('Informe um valor de massa em quilogramas:'))
conversao = quilogramas / 0.45

print(f'Esse massa convertida em libras, é = {conversao}')
