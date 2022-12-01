"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A
comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábriga
e escreva o custo ao consumidor.

       CUSTO DE FÁBRICA            % DO DISTRIBUIDOR      % DOS IMPOSTOS
       Até R$12.000.00                     5                  isento
Entre R$12.000.00 e R$25.000.00            10                   15
     Acima de R$25.000.00                  15                   20

"""

fabrica = int(input('Informe o custo de fáblica:R$'))

if fabrica < 12000:
    distribuidor = fabrica * 5 / 100
    print(f'O custo do consumidor é:R${fabrica + distribuidor}')
elif 12000 <= fabrica <= 25000:
    distribuidor = fabrica * 10 / 100
    imposto = fabrica * 15 / 100
    print(f'O custo do consumidor é:R${fabrica + distribuidor + imposto}')
elif fabrica > 25000:
    distribuidor = fabrica * 15 / 100
    imposto = fabrica * 20 / 100
    print(f'O custo do consumidor é:R${fabrica + distribuidor + imposto}')
else:
    print('Dados invalidos...')
