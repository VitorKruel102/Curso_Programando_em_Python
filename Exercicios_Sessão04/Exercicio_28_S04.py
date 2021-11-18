"""
#Exercicio 28: Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
numero_01 = float(input('Primeito valor:'))
numero_02 = float(input('Segundo valor:'))
numero_03 = float(input('Terceiro valor'))

numero01_quadrada = numero_01 ** 2
numero02_quadrada = numero_02 ** 2
numero03_quadrada = numero_03 ** 2
soma = numero01_quadrada + numero02_quadrada + numero03_quadrada

print(f'Primeiro número = {numero01_quadrada} \nSegundo valor = {numero02_quadrada} '
      f'\nTerceiro valor = {numero03_quadrada} \nSoma = {soma}')
