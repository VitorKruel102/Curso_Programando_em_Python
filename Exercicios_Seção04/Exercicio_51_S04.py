"""
#Exercicio 51: Esqueva um programa que leias as coordenadas x e y de pontos no R² e calcule a distãncia origem(0,0)
"""
x = int(input('Informe a primeira coordenada:'))
y = int(input('Informe a segunda coordenada:'))
distancia = ((x ** 2) + (y ** 2)) ** 1 / 2

print(f'A distância é: {distancia}')
