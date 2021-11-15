# Estruturas de repetição
# /////////////////////////////////////////////
"""
Loop for :
    - Loop = Estrutuade de repetição;
    - For (para) = Uma dessas estruturas;

Python:
    for item in interavel:
        //Execução do loop

Utilizam os loops para interar sibe sequências ou sobre valores iteráveis.

Exexmplos de ITERÁVEIS:
    - nome = 'Greek'
    - Lista = [2, ,1 ,2 ,2]
    -Ranges :
        numeros = range(1, 10)
"""
# /////////////////////////////////////////////
"""
/////////////////////////////////////////
nome = 'Greek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma Lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando em uma range)
# range(valor_inicial, valor_final + 1)

for numero in range(1, 10):
    print(numero)
///////////////////////////////////////
"""
# /////////////////////////////////////////////
""""

# Enumerate: Ele separa em cada letra/numero referente ao seu indice
nome = 'Greek university'
# ENUMERATE(NOME) = ((O, 'G'), (1, 'E'), (2, 'E'), (3, 'K')....))

for indice, letra in enumerate(nome):
    print(indice)

# Quando não precisamos de um valor, podemos descarta-lo utilizando um underline(_)
for _, letra in enumerate(nome):
    print(indice)

# Traz todo o enumerate.
   for valor in enumerate(nome):
    print(valor)
/////////////////////////////
"""
# /////////////////////////////////////////////
"""
quantidade = int(input('Quantas vezes todar o loop:'))
for vezes in range(1, quantidade+1):
    print(f'Imprimindo {vezes}')
/////////////////////////////////
quantidade = int(input('Quantas vezes todar o loop:'))
soma = 0
for vezes in range(1, quantidade+1):
    num = int(input(f'Informe o {vezes}/{quantidade} valor:'))
    soma = soma + num
print(f'A soma é {soma}')
////////////////////////////////////
nome = 'Greek university'
for letra in nome:
    print(letra, end='')  # Escreve tudo na mesma linha
////////////////////////////////////

"""
# /////////////////////////////////////////////
"""
# Emoji
# Original:U+1F601
# Modificado : U0001F601

for num in range(1, 10):
    print('\U0001F601' * num)
"""