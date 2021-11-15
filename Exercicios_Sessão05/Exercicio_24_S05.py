"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto
sobre o produto:
    - MG 7%;
    - SP 12%;
    - RJ 15%;
    - MS 8%;
Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do
produto acrescido do imposto do estado em que ele será vendido. Se o estado difitado não for válido, mostre uma mensagem
de erro.
"""
estado = str(input('Informe o seu estado entre as opções: \nMG \nSP \nRJ \nMS \nQual o estado?'))
valor = float(input('Informe o valor do produto:R$'))

if estado.upper() == 'MG':
    print(f'O valor final é:{valor + (valor * 7 / 100)}')
elif estado.upper() == 'SP':
    print(f'O valor final é:{valor + (valor * 12 / 100)}')
elif estado.upper() == 'RJ':
    print(f'O valor final é:{valor + (valor * 15 / 100)}')
elif estado.upper() == 'MS':
    print(f'O valor final é:{valor + (valor * 8 / 100)}')
else:
    print('Os dados são invalidos')




