"""
#Exercicio 15: Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:
G = R * 180/pi, sendo G o ângulo em graus e R em radianos e PI = 3.14
"""
radiando = float(input('Informe o ângulo em radiando:'))
pi = 3.14
conversao = radiando * 180 / pi

print(f'Esse ângulo em radianos = {conversao}')
