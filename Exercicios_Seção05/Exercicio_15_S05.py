"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""
number = int(input('Informe o número entre 1 e 7:'))


if number == 1:
    print('Domingo')
elif number == 2:
    print('Segunda-feira')
elif number == 3:
    print('Terceira-feira')
elif number == 4:
    print('Quarta-feira')
elif number == 5:
    print('Quinta-feira')
elif number == 6:
    print('Sexta-feira')
elif number == 7:
    print('Sábado')
else:
    print('Número invalido')
