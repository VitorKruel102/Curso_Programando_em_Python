"""
===============================================

                Try e Except

===============================================
"""
try:
    len('5')
except NameError as erro_name:
    print(f'A aplicação gerou o seguinte erro: {erro_name}')
except TypeError as erro_type:
    print(f'A aplicação gerou o seguinte erro: {erro_type}')
except:
    print('Outro erro...')

def pega_valor(dicionario, chave):
    """."""
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    
dic = {'NOME': 'Geek'}
print(pega_valor(dic, 8))
