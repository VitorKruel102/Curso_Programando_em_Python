"""
#Exercicio 35: Sejam A e B os catetos de um triãngulo, onde a hipotenusa é obtida pela equação:
hipotenusa = Raiz(a² + b²). Faça um programa que receba os valores de A e B e calcule o valor da hipotenusa
da equação. Imprimir o resultado dessa operação.
"""
a = float(input('Informe o primeiro cateto:'))
b = float(input('Informe o segundo cateto:'))
hipotenusa = (a ** 1 / 2) + (b ** 1 / 2)

print(f'A hipotenusa é:{hipotenusa}')
