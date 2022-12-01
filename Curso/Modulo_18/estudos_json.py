"""
JSON - JavaScript Object Notation
API - Meios de comunicação entre os serviços e Desenvolvedores.
"""
import json
import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')
ret = jsonpickle.encode(felix)
print(ret)