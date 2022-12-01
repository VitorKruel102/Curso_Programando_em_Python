"""
Faça um programa que calcule e mostre a área de um trapézio, sabe-se que:
    - A = (basemaior + basemenor) * altura / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
basemaior = float(input('Informe a base maior do trapézio:'))
basemenor = float(input('Informe a base menor do trapézio:'))
altura = float(input('Informe a altura do trapézio:'))
trapezio = ((basemaior + basemenor) * altura) / 2

print(f'A base do trapézio é:{trapezio}')
