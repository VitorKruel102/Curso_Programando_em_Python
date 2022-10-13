"""
===============================================

            List Comprehension

===============================================
"""
numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(pares)
print(impares)