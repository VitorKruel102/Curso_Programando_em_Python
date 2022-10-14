"""
===============================================

    Expressões Lambdas e Funções integradas

===============================================
"""

# Função python:
def funcao(x):
    """."""
    return 3 * x + 1

# Função lambda:
calculo = lambda x: 3 * x + 1
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
hello = lambda : 'Olá'

nomes = ["Vitor Kruel", "Paulo Jahn", "Vitoria Dias", "Vania Renner", "Julia Kruel"]
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())


print(nomes)

print(nome_completo(' Vitor', 'Kruel'))
print(calculo(4))
print(calculo(7))
print(hello())