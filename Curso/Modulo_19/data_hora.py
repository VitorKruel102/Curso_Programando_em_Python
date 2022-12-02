"""
Manipulando Data e Hora:

Biblioteca datetime

"""

import datetime

def exemplos_datetime():
    """Algumas funcionalidades do datetime."""
    print(dir(datetime))
    print(datetime.MAXYEAR)
    print(datetime.MINYEAR)
    print(datetime.datetime.now())
    print(repr(datetime.datetime.now()))

def ajustes_data_hora():
    """Realiza ajuste com o metodo replace."""    
    inicio = datetime.datetime.now()
    print(inicio)
    inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
    print(inicio)
    
def criar_data_hora():
    """."""
    evento = datetime.datetime(2019, 1, 1, 0)
    print(evento)

def tranformando_string_em_data():
    """."""
    nascimento = input('Informe a data de nascimento (dd/mm/yyyy): ')
    nascimento = nascimento.split('/')
    nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
    print(nascimento)
     
def delta_data_e_hora():
    """É a diferença entre duas datas."""
    data_hoje = datetime.datetime.now()
    aniversario = datetime.datetime(2023, 1, 19, 0)
    delta = aniversario - data_hoje
    print(delta)

def acrescenta_delta():
    """É a diferença entre duas datas."""
    data_hoje = datetime.datetime.now()
    regra_boleto = datetime.timedelta(days=3)
    print(data_hoje + regra_boleto)


def metodos_datetime():
    """."""
    agora = datetime.datetime.now() #Podemos especificar o timezone;
    hoje = datetime.datetime.today()

def preparar_manutencao():
    manutentacao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
    print(manutentacao)

def encontrar_dia_semana():
    manutentacao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
    print(manutentacao.weekday())

    """
    0 = Segunda
    1 = Terça
    2 = Quarta
    3 = Quinta
    4 = Sexta
    5 = Sabado
    6 = Domingo
    """
def formatar_data_hota_strftime():
    agora = datetime.datetime.now()
    agora = agora.strftime('%d/%m/%Y')
    print(agora)

def string_to_datetime():
    nascimento = input('Informe a data de nascimento (dd/mm/yyyy): ')
    nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
    print(nascimento)
    print(type(nascimento))

string_to_datetime()