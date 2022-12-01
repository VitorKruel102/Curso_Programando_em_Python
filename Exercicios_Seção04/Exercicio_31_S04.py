"""
#Exercicio 31: Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
numero = int(input('Informe um número inteiro:'))
numero_anterior = numero - 1
numero_sucesor = numero + 1

print(f'O número que você informou é {numero}. \nO antecessor é {numero_anterior} e o sucessor é {numero_sucesor}')
