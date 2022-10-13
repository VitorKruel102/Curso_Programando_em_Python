"""
===============================================

                Funções args

===============================================
"""

def soma_todos_argumentos_1(numero_1, numero_2, numero_3):
    """."""
    return numero_1 + numero_2 + numero_3

def soma_todos_argumentos_2(*args):
    """."""
    return sum(args)

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem é...'

numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_argumentos_2(*numeros)) # Realiza o despacotamento da lista

print(soma_todos_argumentos_2())
print(soma_todos_argumentos_2(4))
print(soma_todos_argumentos_2(4, 6))
print(soma_todos_argumentos_2(4, 6, 9))
print(soma_todos_argumentos_2(4, 6, 9, 10))