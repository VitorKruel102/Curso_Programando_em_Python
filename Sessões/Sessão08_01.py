"""
===============================================

            Funções de Retorno   

===============================================
"""
def quadrado_de_7():
    """."""
    return (7 * 7)

def diz_oi():
    """."""
    return 'Oi!'

def nova_fincao():
    """."""
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2

    return 'b'

def outra_funcao():
    """."""
    return 1, 2, 3, 4

def joga_moeda():
    """Gera um número randomico entre 0 e 1."""
    from random import random

    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

def eh_impar():
    """."""

    numero =5
    if numero % 2 != 0:
        return True
    return False

um, dois, tres, quatro = outra_funcao()
quadrado = quadrado_de_7()
oi = diz_oi()

print(f'Retorno: {joga_moeda()}')