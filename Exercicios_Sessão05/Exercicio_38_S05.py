"""
Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: DIA, MÊS E ANO.

Teste a validade desta data para saber se esta é uma data válida.

Teste se o dia fornecido é um dia válido: DIA > 0, DIA <=28 para o mês de fevereiro(29 se o ano for bissexto), DIA <=30
em abril, junho, setembro e novembro, dia <= 31 nos outros meses.

Teste a validade do ano: ANO <= ANO ATUAL (Use uma constante definida com o valor igual a 2008) imprimir: 'Data válida'
ou 'Data inválida' no final da execução do programa.

"""

dia = int(input('Informe a dia de nascimento:'))
mes = int(input('Informe o mes de nascimento:'))
ano = int(input('Informe o ano de nascimento:'))
anoatual = 2021

valida = False

if dia > 0 and ano <= anoatual:

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            valida = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            valida = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29:
                valida = True
        elif dia <= 28:
            valida = True
if valida:
    print('Data valida')
else:
    print('Data Inválida')
