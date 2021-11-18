"""
#Exercicio 39: A importãncia de R$780.000.00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
    - O primeiro ganhador receberá 46%;
    - O segundo receberá 32%;
    - o terceiro recebera o restante;
Calcule e imprima a quantia ganhada por cada um dos vencedores
"""
premio = 78000000
primeiro = premio * 46 / 100
segundo = premio * 32 / 100
terceiro = premio - primeiro - segundo

print(f'Prémio do primeiro colocado:R${primeiro} \nO segundo ganhará:R${segundo} \nO terceiro ficará com: R${terceiro}')
