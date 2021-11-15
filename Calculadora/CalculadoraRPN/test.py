"""
StringIO = é uma classe Python que representa strings em estruturas que se comportam como se
fossem arquivos (com a mesma interface dos objetos file), mas que ficam residentes em
memória, como strings comuns. Isso pode ser útil quando lidamos com APIs cuja interface exige
objetos file.
"""

operacao = input()

while operacao != 'exit':

    pilha = [operacao]
    for x in pilha:
        if isinstance(x, int):
            pilha.append(operacao)
        elif x == str and x == '+':
            x = pilha.pop()
            y = pilha.pop()
            pilha.append(x + y)
        elif x == str and x == '-':
            x = pilha.pop()
            y = pilha.pop()
            pilha.append(x - y)
        elif x == str and x == '*':
            x = pilha.pop()
            y = pilha.pop()
            pilha.append(x * y)
        elif x == str and x == '/':
            x = pilha.pop()
            y = pilha.pop()
            pilha.append(y / x)
        else:
            invali = pilha.pop()
