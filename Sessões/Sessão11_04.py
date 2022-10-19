"""
===============================================

            Python Debugger

===============================================
"""
# Forma mais amadora de debuggar (print())
def dividir(a, b):
    """."""
    print(f'a: {a}\nb: {b}')
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Precisa ser um número númericico'
    except ZeroDivisionError:
        return 'Não podemos dividir por 0'

    
# Forma mais profissional de debuggar  
nome = 'Vitor'
sobrenome = 'Kruel'
breakpoint()
nome_completo = nome + '' + sobrenome
curso = 'Python'
final = nome_completo + ' Faz o curso em' + curso
print(final)

