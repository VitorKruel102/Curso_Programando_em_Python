"""
===============================================

            Funções com Parametros

===============================================
"""

def quadrado(numero = int()):
    """."""
    return (numero ** 2)

def cantar_parabens(aniversariante = None):
    """."""
    print(
        f'''
        Parabéns pra você,
        Nesta data querida
        Muitas felicidades
        Muitos anos de vida
        Viva o/a {aniversariante}!
        '''
    )

def soma(a, b):
    """."""
    return a + b

def multiplica(numeor_1, numero_2):
    """."""
    return numeor_1 * numero_2

def outra(numero_1, b, msg):
    """."""
    return (numero_1 + b) * msg

def nome_completo(nome, sobrenome):
    """."""
    return f'Seu nome completo é {nome} {sobrenome}'

def soma_impares(numeros):
    """."""
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    
    return total

print(nome_completo(nome='Vitor', sobrenome='Kruel'))
