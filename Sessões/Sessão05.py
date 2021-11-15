
# Estrutura condicionais

"""
Estrutura:
    if = Se
    Else = Se não
    Elif = Se não se
///////////////
if 6 > 4:
    print('maior que')
///////////////
number = 6

if number > 4:
    print('maior que')
else:
    print('menor que')
///////////////
number = 6

if number > 4:
    print('maior que')
elif number == 5:
    print('igual')
else:
    print('menor que')
///////////////
"""

# Estruturas Lógicas

"""
Operadores unário:
    -not 
    -is  (O valor precisa ser invertido)
Operadores Binarios:
    -and (Os dois precisão ser verdadeiros)
    -or  (Um ou outro precisa estar verdadeiro)
///////////////    
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo(a)')
else:
    print('Acesso negado')
///////////////
ativo = True
logado = True

if not ativo: #Se não estiver ativo, então:
    print('Bem-vindo(a)')
else:
    print('Acesso negado')
///////////////
ativo = True
logado = True

if ativo is True:
    print('Bem-vindo(a)')
else:
    print('Acesso negado')
///////////////

"""

ativo = True
logado = True

if ativo is True:
    print('Bem-vindo(a)')
else:
    print('Acesso negado')
