"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a
comissão, considere a tabela abaixo.

        VENDA MENSAL                        COMISSÃO
       >= R$100.000.00             R$700.00 + 16% das vendas
< R$100.000.00 >= R$80.000.00      R$650.00 + 14% das vendas
 < R$80.000.00 >= R$60.000.00      R$600.00 + 14% das vendas
 < R$60.000.00 >= R$40.000.00      R$550.00 + 14% das vendas
 < R$40.000.00 >= R$20.000.00      R$500.00 + 14% das vendas
        < R$20.000.00              R$400.00 + 14% das vendas
"""

valor = float(input('Informe o valor da venda:'))

if valor >= 10000000:
    print(f'Sua comissão é:R${700 + (valor * 16/100)}')
elif 10000000 < valor >= 8000000:
    print(f'Sua comissão é:R${650 + (valor * 14 / 100)}')
elif 8000000 < valor >= 60000000:
    print(f'Sua comissão é:R${600 + (valor * 14 / 100)}')
elif 60000000 < valor >= 40000000:
    print(f'Sua comissão é:R${550 + (valor * 14 / 100)}')
elif 40000000 < valor >= 20000000:
    print(f'Sua comissão é:R${500 + (valor * 14 / 100)}')
else:
    print(f'Sua comissão é:R${400 + (valor * 14 / 100)}')
