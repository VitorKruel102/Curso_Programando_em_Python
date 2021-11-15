"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
    - infantil A = 5-7 idades;
    - infantil b = 8-10 idades;
    - juvenil A = 11-13 idades;
    - juvenil B = 14-17 idades;
    - sênior = maior de 18ANOS idades;
"""

idade = int(input('Informe sua idade:'))

if 5 <= idade <= 7:
    print('Sua categoria é infantil A')
elif 8 <= idade <= 10:
    print('Sua categoria é infantil B')
elif 11 <= idade <= 13:
    print('Sua categoria é juvenil A')
elif 14 <= idade <= 17:
    print('Sua categoria é juvenil B')
elif idade >= 18:
    print('Sua categoria é sênior')
else:
    print('Você ainda não tem idade para competir...')
