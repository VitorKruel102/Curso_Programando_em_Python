"""
===============================================

        Leitura de arquivos com With

===============================================
"""
diretory = r'C:\Users\diaxt\Desktop\Python\Udemy\ProgramadoPython\ExerciciosPython\Sessões\escreve.txt'

def leitura():
    """."""
    with open(diretory) as csv_file:
        print(csv_file.readlines())

def escrevendo():
    with open(diretory, 'w', newline='') as csv_file:
        csv_file.write('Info...')

def adicionando_nota():
    with open(diretory, 'a', newline='') as csv_file:
        csv_file.write('Info...')