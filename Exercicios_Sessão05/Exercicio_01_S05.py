# Faça um programa que receba dois números e mostre qual deles é o maior.

number00 = float(input('Digite um número:'))
number01 = float(input('Digite outro número:'))

if number00 > number01:
    print(f'{number00} é o maior número!')
elif number00 == number01:
    print(f'{number00} é igual {number01}')
else:
    print(f'{number01} é o maior número!')
