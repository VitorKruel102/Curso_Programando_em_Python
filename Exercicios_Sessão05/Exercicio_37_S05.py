"""
As tarifas de certo parque de estacionamento são as seguintes:
    - 1 e 2 hora - R$1.00 Cada
    - 3 e 4 hora - R$1.40 Cada
    - 5hora e seguintes - R$2.00 Cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos
pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos.

Os momentos de chegada ao parque e partida deste são apresentados na forma de pares internos, representando horas e
minutos.Por exemplo, o par 12 50 representará "dez para uma da tarde".

Pertende-se criar um programa que, lidos pelo teclado os momentos de chegada e partida, escreva na tela o preço cobrado
pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas.

Portanto, se uma dada hora de chegara for superior à da partida, isso não é uma situação de erro, antes significará que
a partida ocorreu no dia seguinte ao da chegada.
"""
