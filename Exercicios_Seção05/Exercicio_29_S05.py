"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha
números aleatórios entre 1 e 100, e mostre na tela a pergunta. Faça cinco perguntas ao aluno, e mostre para ele as
perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
"""
print('Bem-vindo(a), sua prova tem 5 perguntas. \nBoa prova!!')
pergunta01 = float(input('Questão 01: \n2 + 5 ='))
pergunta02 = float(input('Questão 02: \n2 + 10 ='))
pergunta03 = float(input('Questão 03: \n5 + 5 ='))
pergunta04 = float(input('Questão 04: \n55 + 5 ='))
pergunta05 = float(input('Questão 05: \n80 + 9 ='))
print('Resultado:')
lista = []

if pergunta01 == 7:
    pergunta01 = 1
    print('2 + 5 = 7')
    lista.append(pergunta01)
if pergunta02 == 12:
    pergunta02 = 1
    print('2 + 10 = 12')
    lista.append(pergunta02)
if pergunta03 == 10:
    pergunta03 = 1
    print('5 + 5 = 10')
    lista.append(pergunta03)
if pergunta04 == 60:
    pergunta04 = 1
    print('55 + 5 = 60')
    lista.append(pergunta04)
if pergunta05 == 89:
    pergunta05 = 1
    print('80 + 9 = 89')
    lista.append(pergunta05)

soma = sum(lista)
print(f'você acertou:{soma}')


