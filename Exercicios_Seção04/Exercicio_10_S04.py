"""
#Exercicio 10: Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo)
a fórmula de convensão é: M = K/3.6, sendo K a velovidade em Km/h e M em m/s.
"""
velocidade = float(input('Dígite a sua velocidade em Km/h:'))
conversao = velocidade / 3.6

print(f'a velocidade em m/s é = {conversao}')
