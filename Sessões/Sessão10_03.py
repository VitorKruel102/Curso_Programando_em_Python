"""
===============================================

                    Filter

===============================================
"""
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)

resposta = list(filter(lambda x: x > media, dados))
print(resposta)

paises = [
    "", 
    "Argentina", 
    "", 
    "Brasil", 
    "Chile",
    "", 
    "Colombia", 
    "", 
    "Equador", 
    "", 
    "", 
    "Venezuela"
]

filtro_resposta = list(filter(None, paises))
print(filtro_resposta)