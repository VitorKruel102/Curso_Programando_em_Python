"""
===============================================

            List Comprehension

===============================================
"""
# Loop
numeros = [1, 2, 3, 4, 5]
numero_dobrado = []

for numero in numeros:
    numero_dobrado.append(numero * 2)

print(numero_dobrado)

# List Comprehension
lista_comprehension = [numero * 10 for numero in numeros]
print(lista_comprehension)

