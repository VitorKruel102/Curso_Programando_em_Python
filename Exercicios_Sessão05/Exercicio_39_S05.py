"""
Uma empresa decide dar um aumento aos seus funcionarios de acordo com uma tabela que considera o salário atual e o tempo
de serviço de cada funcionario. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os
funcionarios com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
adicional de salário. Faça um programa que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionario na empresa(número de anos de trabalho na empresa).
Use as tabelas abaixos para calcular o salário reajuste deste funcionário e imprima o valor do salário final reajustado,
ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

 SALARIO ATUAL       REAJUSTE(%)       TEMPO DE SERVIÇO     BÔNUS
  Até 500.00            25%              1 anos      Sem bônus
  Até 1000.00           20%             De 1 a 3 anos       100
  Até 1500.00           15%             De 4 a 6 anos       200
  Até 2000.00           10%             De 7 a 10 anos      300
Acima de 2000.00     Sem reajuste       Mais de 10 anos      500

"""
salario = float(input('Informe o seu sálario:'))
print('Caso não tenha 1 ano trabalhado, digite: 0')
tempo = int(input('Informe os anos trabalhados:'))


if tempo < 1:
    if salario <= 500:
        salario_novo = salario + (salario * 25 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo}')
    elif salario <= 1000:
        salario_novo = salario + (salario * 20 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo}')
    elif salario <= 1500:
        salario_novo = salario + (salario * 15 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo}')
    elif salario <= 200:
        salario_novo = salario + (salario * 10 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo}')
    else:
        print('Infelizmente ainda você não tem reajuste')

elif 1 <= tempo <= 3:
    if salario <= 500:
        salario_novo= salario + (salario * 25 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 100}')
    elif salario <= 1000:
        salario_novo = salario + (salario * 20 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 100}')
    elif salario <= 1500:
        salario_novo = salario + (salario * 15 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 100}')
    elif salario <= 200:
        salario_novo = salario + (salario * 10 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 100}')
    else:
        print(f'Infelizmente ainda você não tem reajuste, mas terá um bônus de {salario + 100}')

elif 4 <= tempo <= 6:
    if salario <= 500:
        salario_novo= salario + (salario * 25 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 200}')
    elif salario <= 1000:
        salario_novo = salario + (salario * 20 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 200}')
    elif salario <= 1500:
        salario_novo = salario + (salario * 15 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 200}')
    elif salario <= 200:
        salario_novo = salario + (salario * 10 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 200}')
    else:
        print(f'Infelizmente ainda você não tem reajuste, mas terá um bônus de {salario + 200}')

elif 7 <= tempo <= 10:
    if salario <= 500:
        salario_novo= salario + (salario * 25 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 300}')
    elif salario <= 1000:
        salario_novo = salario + (salario * 20 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 300}')
    elif salario <= 1500:
        salario_novo = salario + (salario * 15 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 300}')
    elif salario <= 200:
        salario_novo = salario + (salario * 10 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 300}')
    else:
        print(f'Infelizmente ainda você não tem reajuste, mas terá um bônus de {salario + 300}')

elif tempo > 10:
    if salario <= 500:
        salario_novo= salario + (salario * 25 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 500}')
    elif salario <= 1000:
        salario_novo = salario + (salario * 20 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 500}')
    elif salario <= 1500:
        salario_novo = salario + (salario * 15 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 500}')
    elif salario <= 200:
        salario_novo = salario + (salario * 10 / 100)
        print(f'Pelo tempo de trabalho, ainda não será possivel receber um bônus. \n'
              f'Seu novo sálario é:R${salario_novo} e um bônus {salario_novo + 500}')
    else:
        print(f'Infelizmente ainda você não tem reajuste, mas terá um bônus de {salario + 500}')
else:
    print('Dados infalidos...')
