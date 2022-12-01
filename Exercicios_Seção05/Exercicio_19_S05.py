"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente
pelos dois.
"""
number = float(input('Informe um número:'))

if (number % 3 == 0) and (number % 5 != 0):
    print('O número é divisivel por 3')
elif (number % 3 != 0) and (number % 5 == 0):
    print('O número é divisivel por 5')
else:
    print('Número não pode ser divisivel por 3 e 5 simultanemente ou ele não é um número falido.')
