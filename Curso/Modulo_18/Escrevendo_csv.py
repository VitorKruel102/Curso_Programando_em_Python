import csv

def escrevendo_no_csv_com_listas():
    """."""
    with open('filmes.csv', 'w', newline='') as csvfile:
        escritor_csv = csv.writer(csvfile)
        filme = None
        escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])

        while filme != 'sair':
            filme = input('Informe um filme: ')
            ...
            if filme.lower() != 'sair':
                genero = input('Informe o genero: ')
                duracao = input('Informe a duracao: ')
                escritor_csv.writerow([filme, genero, duracao])

def escrevendo_no_csv_com_dicionario():
    """."""
    with open('filmes.csv', 'w', newline='') as csvfile:
        cabecalho = ['Titulo', 'Genero', 'Duracao']
        escritor_csv = csv.DictWriter(csvfile, fieldnames=cabecalho)
        escritor_csv.writeheader()
        filme = None
    
        while filme != 'sair':
            filme = input('Informe um filme: ')
            ...
            if filme.lower() != 'sair':
                genero = input('Informe o genero: ')
                duracao = input('Informe a duracao: ')
                escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao':duracao})

