"""
As tarifas de certo parque de estacionamento são as seguintes:
    - 1 e 2 hora - R$1.00 Cada
    - 3 e 4 hora - R$1.40 Cada
    - 5hora e seguintes - R$2.00 Cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos
pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos.

Os momentos de chegada ao parque e partida deste são apresentados na forma de pares internos, representando horas e
minutos.Por exemplo, o par 12 50 representará "dez para uma da tarde".

Pertende-se criar um programa que,
Portanto, se uma dada hora de chegara for superior à da partida, isso não é uma situação de erro, antes significará que
a partida ocorreu no dia seguinte ao da chegada.
"""


hora_chegada = int(input("Digite a hora de chegada: "))
min_chegada = int(input("Digite o minuto de chegada: "))
hora_partida = int(input("Digite a hora de chegada: "))
min_partida = int(input("Digite o minuto de saída: "))

if hora_chegada > hora_partida:
    hora_partida = hora_partida + 24
if min_chegada > min_partida:
    min_partida = min_partida + 60
    hora_partida = hora_partida - 1

min_final = min_partida - min_chegada
hora_final = hora_partida - hora_chegada

if hora_final >= 1:
    if min_final > 1:
        print(f'O carro ficou estacionado durante {hora_final} horas e {min_final}  minutos.')
    else:
        print(f'O carro ficou estacionado durante {hora_final} horas.')
else:
    print(f'O carro ficou estacionado durante {min_final} minutos.')


min_total = int((hora_final * 60) + min_final)

if min_total <= 120:
    if min_total <= 60:
        preco = 1.00
        print(f'Preço total: R${preco}')
    else:
        preco = 2
        print(f'Preço total: R${preco}')
elif min_total <= 240:
    if min_total <= 180:
        preco = 2 + 1.40
        print(f'Preço total: R${preco}')
    else:
        preco = 2 + (1.40 * 2)
        print(f'Preço total: R${preco}')
else:
    hora_total = int(min_total // 60)
    preco = 4.40 + ((hora_total - 4) * 2)
    print(f'Preço total: R${preco}')



