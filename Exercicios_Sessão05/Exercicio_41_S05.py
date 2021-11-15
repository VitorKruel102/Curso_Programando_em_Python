"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação e mostre sua classificação de acordo com
a tabela abaixos:

     IMC            CLASSIFICAÇÃO
    <18.5           Abaixo do peso
  18.6-24.9           Saudável
  25.0-29.9         Peso em excesso
  30.0-34.9         Obesidade Grau 1
  35.0-39.9         Obesidade Grau 2(severa)
   >=40,0           Obesidade Grau 3(mórbida)
"""
peso = float(input('Informe seu peso (em kg):'))
altura = float(input('Informe seu altura (em metros):'))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Seu peso está abaixo do ideal.')
elif 18.6 <= imc <= 24.9:
    print('Você está com o peso sadável.')
elif 25 <= imc <= 29.9:
    print('Você está com o peso em excesso.')
elif 30 <= imc <= 34.9:
    print('Você está com o peso com Obesidade Grau 1.')
elif 35 <= imc <= 39.9:
    print('Você está com o peso com Obesidade Grau 2(severa).')
elif imc >= 40:
    print('Você está com o peso com Obesidade Grau 3(mórbida).')
else:
    print('Dados Invalidos...')
