"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em percurso, calcule o consumo em
km/l e escreva uma mensagem de acordo com a tabela abaixo:
    - Menor que 8km/l ("Venda o carro")
    - Entre 8-14km/l ("Ecnonômico")
    - maior que 14km/l ("Super ecnonômico")
"""
distancia = float(input('Comparação da relação do gasto de gasolina e a distancia: '
                  '\nInforme a distancia percorrida(km):'))
gasolina = float(input('Informe quantos litros foram consumidos(L):'))

tabela = distancia / gasolina

if tabela <= 8:
    print('Venda o carro')
elif 8 < tabela <= 14:
    print('Econôomico')
elif tabela > 14:
    print('Super econômico')
else:
    print('Dados invalidos')
