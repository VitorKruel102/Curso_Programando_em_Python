"""
Calcule as raízes da equação de 2°grau. Lembre-se:
        x = -b +- RAIZ(delta) / 2a
               onde:
          Delta = B² - 4ac

E ax² + bx + c = 0 representa uma equação de 2²graus.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
    - Se DELTA < 0, não existe real. Imprima a mensagem "Não existe raiz".
    - Se DELTA = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única".
    - Se DELTA >= 0, imprima as duas raizes reais.
"""
a = int(input('Informe o valor de a:'))
b = int(input('Informe o valor de b:'))
c = int(input('Informe o valor de c:'))

delta = (b ** 2) - (4 * a * c)
x1 = (-b + (delta ** 1 / 2)) / (2 * a)
x2 = (-b - (delta ** 1 / 2)) / (2 * a)

if delta < 0:
    print('Não existe raiz')
elif delta == 0:
    print(f'A raiz é {x1}, é uma raiz única.')
else:
    print(f'x1:{x1} e x2:{x2}')
