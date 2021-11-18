"""
#Exercicio 43: Escreva um programa de ajuda para vendedores. A partir de um valor total lidom mostre:
    - O total a pagar com desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
    - A comissão do vendedos, no caso da venda parcelada(5% sobre o valor total)
"""
preco = float(input('Informe o valor do produto escolhido:R$'))
desconto = 10
parcela = 3
comissao = 5
avista = preco - (preco * desconto / 100)
parcelada = preco / parcela
comissao_vista = avista * comissao / 100
comissao_parcelada = preco * comissao / 100

print(f'O valor a vista:R${avista} \nValor parcelado: {parcela}x de R${parcelada}')
print(f'A comissão(A vista):R${comissao_vista} \nComissão(parcelado):R${comissao_parcelada}')
