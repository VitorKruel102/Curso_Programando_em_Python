"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for disponivel por 400 ou se for
disponivel por 4 e não for dispponivel por 100. Por exemplo: 1988, 1992, 1996.
"""
ano = int(input('Informe o ano:'))

if ano % 4 == 0:
    print('O ano é bissexto')
else:
    print('Não é bissexto')
