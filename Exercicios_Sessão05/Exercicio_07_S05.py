"""
Faça um programa que recaba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a
mensagem "Número iguais"
"""
number01 = float(input('Dígite o primeiro número:'))
number02 = float(input('Dígite o segundo número:'))

if number01 > number02:
    print(f'O maior número é:{number01}')
elif number01 == number02:
    print(f"Números são iguais")
else:
    print(f'O maior número é:{number02}')
