"""
Serialização/deserialização

Tranformar em:
Objeto python -> Binarização 
Binarização -> Objeto python

pickle = "Salva dados como um banco de dados em um formato binario"
 
"""
import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    def comer(self):
        print(f"{self.nome} está comendo...")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def min(self):
        print(f"{self.nome} esta miando...")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def late(self):
        print(f"{self.nome} esta latindo...")

felix = Gato('Felix')
pluto = Gato('Pluto')

def escrita_picke():
    """Realiza a Serialização, passando os dados para binario."""
    with open('animais.pickle', 'wb') as arquivo:
        pickle.dump((felix, pluto), arquivo)

def leitura_picke():
    """Realiza a Deserialização, passando os dados para texto."""
    with open('animais.pickle', 'rb') as arquivo:
        gato, cachorro = pickle.load(arquivo)
        print(gato, cachorro)
    
leitura_picke()