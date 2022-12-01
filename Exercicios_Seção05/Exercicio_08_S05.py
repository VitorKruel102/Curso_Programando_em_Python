"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
Uma nota válida deve ser, obrigatóriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua valor válido, este
fato deve ser informado ao usuário e programa termina.

Outro metodo:
if 10 > nota01 > 0 and 10 > nota02 > 0:
    med = (nota01 + nota02) / 2
    print(f'Média:{med}')
else:
    print("As notas são invalidas")

"""

nota01 = float(input('Informe a primeira nota:'))
nota02 = float(input('Informe a segunda nota:'))

if nota01 <= 10 and nota01 >= 0:
    if nota02 <= 10 and nota02 >= 0:
        med = (nota01 + nota02) / 2
        print(f'Média:{med}')
    else:
        print("As notas são invalidas")
