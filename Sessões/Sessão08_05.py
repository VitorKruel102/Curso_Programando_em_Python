"""
===============================================

                Funções **kwargs

===============================================
"""
def cores_favoridas(**kwargs):
    """."""
    for pessoa, cor in kwargs.items():
        print(f'A cor favorida de {pessoa.title()} é {cor}')

def cumprimento_especial(**kwargs):
    """."""
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Vodê recebeu um cumprimento pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não renho certeza quem você é . . ."

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    """."""
    print(f'{nome.title()} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Vitor')
minha_funcao(8, 'Vitor', 1, 2, 3, solteiro=True)
minha_funcao(8, 'Vitor', eu='Não', voce='vai')
minha_funcao(8, 'Vitor', 1, 2, 3, java=False, python=True)
