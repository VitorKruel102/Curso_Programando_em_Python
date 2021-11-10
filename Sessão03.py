"""
print('Bem vindo(a) %s' % name) #Antigo
print('Bem vindo(a) {0}'.format(name)) #Moderno
print(f'Bem vindo(a) {name}') #Super Moderno

Input = Todo dado recebido no input é uma string

"""

name = str(input('Nome:'))
idade = int(input('Idade:'))
andress = input('Endereço:')
cep = int(input('CEP:'))

print('loading')
print('Direcionando para a página')
print(f'Bem vindo(a) {name}')
print(f'Endereço: {andress} e Cep: {cep}')
print(f'nasceu em {2021 - idade}')
