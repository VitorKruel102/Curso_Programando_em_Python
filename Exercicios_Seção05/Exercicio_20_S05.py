"""
Dados três valores A, B, C. Verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo
escaleno, equilátero ou isósceles, considerenado os seguintes conceitos:
    - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados;
    - Chama-se equilátero o triângulo que tem três lados iguais.
    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - Recebe o nome de escaleno o triãngulo que tem os três lados diferentes.
"""
a = float(input('Informe o primeiro lado do triângulo:'))
b = float(input('Informe o valor do segundo lado:'))
c = float(input('Informe o terceiro lado:'))

if a + b > c or b + c > a or c + a > b:
    if a == b and b == c:
        print('Equilátero')
    elif a == b or b == c or c == a:
        print('Isósceles')
    else:
        print("Escaleno")
