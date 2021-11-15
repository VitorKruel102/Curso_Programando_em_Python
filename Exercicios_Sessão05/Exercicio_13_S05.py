"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser igual ou superios a 60 pontos.
"""

nota00 = float(input('Informe a primeira nota:'))
nota01 = float(input('Informe a segunda nota:'))
nota02 = float(input('Informe a terceira nota:'))

med = (nota00*1 + nota01*1 + nota02*2) / (1 + 1 + 2)

if med >= 60 and med <= 70:
    print(f'Sua nota foi:{med} \nVocê está aprovado!Atingiu o limite satisfatório...')
elif med >= 71 and med <= 85:
    print(f'Sua nota foi:{med} \nVocê está aprovado!Atingiu o nível desejado...')
elif med >= 86 and med <= 100:
    print(f'Sua nota foi:{med} \nVocê está aprovado!Parabéns, você ficou entre os melhores da sua turma.')
else:
    print(f'Sua nota foi:{med} \nVocê está reprovado...')
