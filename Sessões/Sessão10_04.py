"""
===============================================

                    Reduce

===============================================
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

def funcao(x, y):
    """."""
    return x * y

# Reduce
resultado = reduce(funcao, dados)
print(resultado)

# Loop
resposta = 1
for n in dados:
    resposta = resposta * n
print(resposta)