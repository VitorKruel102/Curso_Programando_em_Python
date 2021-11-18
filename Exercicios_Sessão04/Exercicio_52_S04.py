"""
#Exercicio 52: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""
amigo01 = input('Amigo 01:')
investimento_amigo01 = float(input('Informe o seu investimento:R$'))
amigo02 = input('Amigo 02:')
investimento_amigo02 = float(input('Informe o seu investimento:R$'))
amigo03 = input('Amigo 03:')
investimento_amigo03 = float(input('Informe o seu investimento:R$'))
premio = float(input('Qual o valor do prêmio:R$'))

aposta_total = investimento_amigo01 + investimento_amigo02 + investimento_amigo03
premio_amigo01 = investimento_amigo01 / aposta_total
premio_amigo02 = investimento_amigo02 / aposta_total
premio_amigo03 = investimento_amigo03 / aposta_total
recebe_amigo01 = premio * premio_amigo01
recebe_amigo02 = premio * premio_amigo02
recebe_amigo03 = premio * premio_amigo03

print(f'O {amigo01} recebe {recebe_amigo01} \nO {amigo02} recebe {recebe_amigo02} '
      f'\nO {amigo03} recebe {recebe_amigo03}')
