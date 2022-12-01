

class Lampada:
    def __init__(self, cor, voltagem, luminosidade): # Método construtor
        self.__voltagem = voltagem # Atributos
        self.__cor = cor # Atributos
        self.__luminosidade = luminosidade # Atributos
        self.__ligada = False # Atributos


class ContaCorrente:
    contador = 1234
    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produtos:
    
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produtos.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = (valor + Produtos.imposto)
        Produtos.contador = self.id

    def desconto(self, porcentagem): # Mêtodo de Instancia 
        """Retorna o valor do produto com desconto."""
        return (self.__valor * (100 - porcentagem)) / 100


ps = Produtos('massa', 'integral', 5.50)
ps.peso = '5kg'
del ps.peso
print(ps.__dict__)


class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def __corre__(self, metros):
        print(f'{self.__nome} está correndo {metros} metros.')



class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        Conta.contador += 1
    

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Métodos públicos 
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self): # Método periogoso, altera os valores
        self.__limite = limite


conta_1 = Conta('Vitor', 4000, 5000)
conta_2 = Conta('Vitória', 5000, 6000)