"""
#Exercicio 17: Leia um valor de comprimento em centímetros e apresente-o convertido em poldegadas.
A fórmula de conversão é: P = C/2.52, sendo C o comprimento em centímetros e P o comprimento em polegadas
"""
centimetros = float(input('Informe o comprimento em centímetros:'))
conversao = centimetros / 2.52

print(f'Esse comprimento em poldegadas é = {conversao}')
