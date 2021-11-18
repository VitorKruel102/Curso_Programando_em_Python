"""
#Exercicio 36: Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um
cilindro circular é calculado por meio da seguinte fórmula: V = PI * raio² * altura, onde PI = 3.141592
"""
altura = float(input('Informe a altura do cilindro:'))
raio = float(input('Informe também o raio do cilindro:'))
pi = 3.141592
volume = pi * (raio ** 2) * altura

print(f'O volume do cilindro é:{volume}')
