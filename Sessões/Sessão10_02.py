"""
===============================================

                    Map

===============================================
"""
import math

# Função python:
def area(raio):
    """Calcula a área de um círculo com raio"""
    return math.pi * (raio ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]
areas = list(map(area, raios))

# Map com Lambda:
areas_map = list(map(lambda raio: math.pi * (raio ** 2), raios))

print(areas)
print(areas_map)
print(area(2))
print(area(5.3))
