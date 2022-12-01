"""
#Exercicio 48: Leia um valor inteiro em segundo, e imprima-o em horas, minutos, e segundo.
"""
number = int(input('Informe valor em segundos:'))
hora = number / 3600
minuto = number / 60

print(f'Hora:{hora} \nMinuto:{minuto} \nSegundos:{number}')
