"""
===============================================

                Any e All

===============================================
"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all([0]))
print(all([1, 2, 3, 4]))
print(all([]))

print(any([nome[0] == 'C' for nome in nomes]))
print(any([0]))
print(any([1, 2, 3, 4]))
print(any([]))