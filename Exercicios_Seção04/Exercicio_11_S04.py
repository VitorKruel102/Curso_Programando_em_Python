"""
#Exercicio 11: Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em Km/hs (quilômetros por hora)\
a fórmula de convensão é: K = M*3.6, sendo K a velovidade em Km/h e M em m/s.
"""
velocidade = float(input('Dígite a sua velocidade em m/s:'))
conversao = velocidade * 3.6

print(f'A velocidade em Km/h é = {conversao}')
