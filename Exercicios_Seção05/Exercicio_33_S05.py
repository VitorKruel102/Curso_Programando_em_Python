"""
Um produto vai sofrer um aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e
escreva uma mensagem em função do preço novo(De acordo com a segunda tabela).

    PREÇO ANTIGO    PERCENTUAL DE AUMENTO           PREÇO NOVA         MENSAGEM
     Até R$50                5%                      Até R$80           Barato
   R$50 e R$100              10%                    R$80 e R$120        Normal
   Acima R$100               15%                    R$120 e R$200        Caro
                                                    Acima R$200       Muito Caro
"""
antigo = int(input('Informe o preço do produto para o reajuste:'))

if antigo > 0:
    if antigo < 50:
        print(f'A novo valor é:{antigo + (antigo * 5 / 100)} \nO produto está barato.')
    if 50 <= antigo <= 100:
        novo = antigo + (antigo * 10 / 100)
        if novo <= 80:
            print(f'A novo valor é:{novo} \nO produto está barato.')
        else:
            print(f'A novo valor é:{novo} \nO produto está com preço Normal.')
    if antigo > 100:
        novo = antigo + (antigo * 15 / 100)
        if 80 < novo <= 120:
            print(f'A novo valor é:{novo} \nO produto está com preço Normal.')
        elif 120 < novo <= 200:
            print(f'A novo valor é:{novo} \nO produto está Caro.')
        elif novo > 200:
            print(f'A novo valor é:{novo} \nO produto está Muito Caro.')
else:
    print('Valor invalido.')
