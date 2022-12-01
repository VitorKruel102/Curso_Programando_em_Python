"""
#Exercicio 32: Lei um número inteiro e imprima a soma do sucessor de seu tiplo com o antecessor de seu dobro.
"""
numero = int(input('Informe um númeor inteiro:'))
sucessor_triplo = (numero * 3) + 1
antecesor_dobro = (numero * 2) - 1
soma = sucessor_triplo + antecesor_dobro

print(f'O número informado é: {numero} \n Resultado = {soma}')
