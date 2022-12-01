"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
respectivamente, a um trabalhado de laboratório, a uma avaliação semestral e a um exame final. A média das três notas
mencionadas anteriormente obedece aos pesos:
    - Trabalho de Laboratório: 2;
    - Avaliação Semestral: 3;
    - Exame Final: 5;
De acordo com o resultado, mostre na tela se o aluno está reprovado(média entre 0 e 2,9), de recuperação(3 e 4.9) ou se
foi aprovado. Faça todoas as verificações necessárias.
"""

nota01 = float(input('Informe a nota do Trabalho Laboratório:'))
nota02 = float(input('Informe a nota da Avaliação Semestral:'))
nota03 = float(input('Informe a nota do Exame Final:'))

if 0 < nota01 >= 10 and 0 < nota02 >= 10:
    if 0 < nota03 >= 10:
        media = (nota01*2 + nota02*3 + nota03*5) / (2 + 3 + 5)
        if media > 4.9:
            print(f'Você foi aprovado. Sua nota foi {media}')
        elif media <= 4.9 and media >= 2.9:
            print(f'Você esta em recuperação. Sua nota foi {media}')
        else:
            print(f'Você reprovado. Sua nota foi {media}')
else:
    print('Número invalido')
