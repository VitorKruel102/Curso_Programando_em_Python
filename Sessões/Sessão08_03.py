"""
===============================================

        Funções com Parametros padrõs

===============================================
"""

def exponencial(numero=4, potencia=2):
    """."""
    return (numero ** potencia)

def soma(numero_1=1, numero_2=1):
    """."""
    return numero_1 + numero_2

def mostra_informacao(nome='Geek', instrutor=False):
    """."""
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor' 
    return f'Olá, {nome}!'

nomes = 'Vitor'
def diz_oi():
    """."""
    global nomes
    return f'Oi! {nomes}'

def fora():
    """."""
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    
    return dentro()

print(fora().__doc__)