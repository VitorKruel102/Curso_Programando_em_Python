"""
#Exercicio 37: Faça um programa que leia o valor de um produto e imprima o valor com desconto, tento em vista
que o desconto foi de 12%.
"""
produto = float(input('Informe o valor do produto:'))
porcentagem = float(input('Informe a porcetagem do desconto(sem %):'))
desconto = produto - (produto * porcentagem / 100)

print(f'O valor do produto com desconto ficou:{desconto}')
