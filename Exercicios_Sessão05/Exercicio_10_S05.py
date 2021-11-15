"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso idela, utilizando as
seguintes fórmulas(onde h corresponde á altura_:
    - homens : (72.7 * h) - 58
    - mulheres : (62.1 * h) - 44.7
"""
altura = float(input('Digite sua altura:'))
sexo = str(input('Digite seu sexo:'))

if sexo.upper() == 'MULHER':
    print(f'Se peso ideal é:{(62.1 * altura)- 44.7}')
else:
    print(f'Seu peso ideal é:{(72.7 * altura)- 58}')
