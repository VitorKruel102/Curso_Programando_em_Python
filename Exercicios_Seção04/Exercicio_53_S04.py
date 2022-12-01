"""
#Exercicio 53: Faça um programa para ler as dimensões de um terreno(comprimento C e largura L), bem como o preço do
metro de tela P. Imprima o custo para cercar esse mesmo terreno.
"""
comprimento = float(input('Informe o comprimento do terreno:'))
largura = float(input('Informe a largura do terrreno:'))
preco = float(input('Informe o valor do metro da tela:'))

valor = (comprimento * largura) * preco

print(f'O custo da tela ficará:R${valor}')
