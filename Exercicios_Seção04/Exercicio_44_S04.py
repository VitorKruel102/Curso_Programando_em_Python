"""
#Exercicio 44: Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantors degraus o usuário deverá subir para atingir seu objetivo.
"""
degrau = float(input('Informe a alturada do degrau:'))
altura = float(input('Qaul a altura que deseja subir?'))
objetivo = altura / degrau

print(f'Você precisa subir {int(objetivo)} degraus')
