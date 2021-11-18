"""
#Exercicio 49: Faça um programa que leia o horário(Hora,minuto e segundo) de inicio e a duração, em segundos,
de uma experiencia biologica. O programa deve resultar com o novo horário(hora, minuto e segundo) do termino da mesma.
"""
print('Preencha os campos abaixo com o horário atual')

hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
duracao = int(input('\nDuração do evento (segundos): '))

segundo_final = (segundo + duracao) % 60
minuto_final = (minuto + (segundo + duracao) // 60) % 60
hora_final = (hora + (minuto + (segundo + duracao) // 60) // 60) % 24

print(f'O fim do evento se dará às {hora_final}h {minuto_final}min e {segundo_final} segundos')
