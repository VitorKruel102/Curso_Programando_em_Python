"""
Calculadora RPN

- Usário vai digitar um numero ou operação;
    - Se colocar primeiro uma operção = 0
- O numero entra em uma lista;
- Se for uma operação, ele soma com o item anterior;
- Se for um numero, ele acrescenta;

"""
import tokenize
from io import StringIO


def info(dados):
    if isinstance(dados, str):
        dados = StringIO(dados)  # Criando um arquivo
        operation = tokenize.generate_tokens(dados.readline)  # retornar um objeto str e mantem a string
        return operation




