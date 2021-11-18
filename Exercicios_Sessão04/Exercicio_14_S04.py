"""
#Exercicio 14: Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
R = G * PI/180, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""
graus = float(input('Informe o ângulo em graus:'))
pi = 3.14
conversao = graus * pi / 180

print(f'Esse ângulo em radianos = {conversao}')
