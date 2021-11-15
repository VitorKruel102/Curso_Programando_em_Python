# Entendendo Ranges
"""
- Precisamos conhecer o loop for para usar os ranges;
- Precisamos conhecer o Ranges para trabalhar melhor com loops for.

RANGE:
    São utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.
"""
# ///////////////////////////////////////
"""
FORMAS GERAIS:

 # Forma 01:
 
    range(valor_de_parada)

OBS(RANGE):
    - Se a gente não informa o valor_de_inicio, ele será como padrão = 0;
    - Se você colocar o número dá parada, ele será o número -1, ou seja, ate vai ate o valor penultimo indicado;
    - E ele sempre será de 1 em 1;

# Exemplo 01:
for num in range(11):
    print(num)
    
/////////////////////////////////////////////

# Forma 02:

    range(valor_de_inicio, valor_de_parada)

OBS(RANGE):
    - Ele iniciará no valor_de_inicio indicado;
    - Se você colocar o número dá parada, ele será o número -1, ou seja, ate vai ate o valor penultimo indicado;
    - E ele sempre será de 1 em 1;
    
# Exemplo 02:
for num in range(1, 11):
    print(num)
    
/////////////////////////////////////////////

# Forma 03:

    range(valor_de_inicio, valor_de_parada, passo)

OBS(RANGE):
    - Ele iniciará no valor_de_inicio indicado;
    - Se você colocar o número dá parada, ele será o número -1, ou seja, ate vai ate o valor penultimo indicado;
    - E ele sempre será de 1 em 1;
    - O passo indica quantos número ele pula em determinado range. Se o passo = 2, então ele pula em 2 em 2;
    
# Exemplo 03:
for num in range(1, 11, 2):
    print(num)
    
/////////////////////////////////////////////

# Forma 04: Igual a forma 3 mais INVERSA (CONTAGEM REGRESSIVA)

    range(valor_de_inicio, valor_de_parada, passo)

OBS(RANGE):
    - Ele iniciará no valor_de_inicio indicado;
    - Se você colocar o número dá parada, ele será o número -1, ou seja, ate vai ate o valor penultimo indicado;
    - E ele sempre será de 1 em 1;
    - O passo indica quantos número ele pula em determinado range. Se o passo = 2, então ele pula em 2 em 2;
    
# Exemplo 03:
for num in range(10, -1, -1):
    print(num)

/////////////////////////////////////////////
"""

# Criando uma lista com RANGE
lista = list(range(11))



