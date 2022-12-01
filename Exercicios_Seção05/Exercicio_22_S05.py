"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são.
    - Ter pelo menos 65 anos;
    - Ou ter trabalhado pelo menos 30 anos;
    - Ou ter pelo menos 60 anos e trabalhando pelo menos 25 anos.
"""

idade = int(input('Informe sua idade:'))
tempo = int(input('Informe o seu tempo de serviço:'))

if idade >= 65:
    print('Já pode aposentar.')
elif tempo >= 30:
    print('Já pode aposentar.')
elif tempo >= 25 and idade >= 60:
    print('Já pode aposentar')
else:
    print('Ainda não pode aposentar.')