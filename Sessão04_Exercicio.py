"""
#Exercicio 01: Faça um programa que leia um número inteiro e imprima.
    number = int(input('Digite um valor:'))
    print(f'O valor que você digitou é {number}')

#Exercicio 02: Faça um programa que leia um número real e imprima.
    number = input('Digite um valor:')
    print(f'O valor que você digitou é {number}')

#Exercicio 03: Peça ao usúario para digitar três valores inteiros e imprima a soma deles.
    number0 = int(input('Digite o primeiro número inteiro:'))
    number1 = int(input('Digite o Segundo número inteiro:'))
    number2 = int(input('Digite o Terceiro número inteiro:'))
    soma = number0 + number1 + number2

    print(f'A soma de {number0} + {number1} + {number2} é {soma}')

#Exercicio 04: Leia um número real e imprima o resultado do quadrado desse número.
    number = float(input('Digite um número para descobrir qual o valor dele ao quadrado:'))
    elev = number**2

    print(f'O número: {number} ao quadrado ficará {elev}')

#Exercicio 05: Leia um número real e imprima a quinta parte deste número
    number = float(input('Digite um número para descobrir qual é a quinta parte deste valor:'))
    div = number/5

    print(f'O número: {number} ao quadrado ficará {div}')

#Exercicio 06: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A formula \
de conversão é F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a tempreratura em Celsius.
    temperature = float(input('Dígite a temperatura em graus Celsius:'))
    fahrenheit = temperature * (9.0/5.0) \
                 + 32.0
    print(f'A sua temperatura em Fahrenheit é {fahrenheit}')

#Exercicio 07: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula \
de conversão é C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a tempreratura em Fahrenheit.
    temperature = float(input('Dígite a temperatura em graus Fahrenheit:'))
    celsius = 5.0*(temperature-32.0)/9.0
    print(f'A sua temperatura em Celsius é {celsius}')

#Exercicio 08: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula \
de conversão é C = k - 273.15, sendo C a temperatura em Celsius e k a tempreratura em Fahrenheit.
    temperature = float(input('Dígite a temperatura em graus Kelvin:'))
    celsius = temperature - 273.15

    print(f'A sua temperatura em Celsius é {celsius}')

#Exercicio 09: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A formula \
de conversão é K = C + 273.15, sendo K a temperatura em Kelvin e C a tempreratura em Celsius.
    temperature = float(input('Dígite a temperatura em graus Celsius:'))
    kelvin = temperature + 273.15

    print(f'A sua temperatura em Kelvin é {kelvin}')

#Exercicio 10: Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo)\
a fórmula de convensão é: M = K/3.6, sendo K a velovidade em Km/h e M em m/s.
    velocidade = float(input('Dígite a sua velocidade em Km/h:'))
    converter = velocidade/3.6

    print(f'a velocidade em m/s é = {converter}')

#Exercicio 11: Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em Km/hs (quilômetros por hora)\
a fórmula de convensão é: K = M*3.6, sendo K a velovidade em Km/h e M em m/s.
    velocidade = float(input('Dígite a sua velocidade em m/s:'))
    converter = velocidade*3.6

    print(f'a velocidade em Km/h é = {converter}')

#Exercicio 12: Leia a distância em milhas e apresente-a convertida em quilometros. A fórmula de conversão: K = 1.6*m\
sendo K a distância em quilômetros e M em milhas.
    velocidade = float(input('Informe sua distancia em milhas:'))
    converter = 1.6*velocidade

    print(f'a distância em Km/h é = {converter}')

#Exercicio 13: Leia a distância em quilometros e apresente-a convertida em milhas. A fórmula de conversão: M = K/1.61\
sendo K a distância em quilômetros e M em milhas.
    velocidade = float(input('Informe sua distancia em quilometros:'))
    converter = velocidade/1.61

    print(f'a distância em milhas é = {converter}')

#Exercicio 14: Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
R = G * PI/180, sendo G o ângulo em graus e R em radianos e PI = 3.14
    graus = float(input('Informe o ângulo em graus:'))
    pi = 3.14
    converter = graus * pi/180

    print(f'esse ângulo em radianos = {converter}')

#Exercicio 15: Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:
G = R * 180/pi, sendo G o ângulo em graus e R em radianos e PI = 3.14
    radiando = float(input('Informe o ângulo em radiando:'))
    pi = 3.14
    converter = radiando * 180/pi

    print(f'esse ângulo em radianos = {converter}')

#Exercicio 16: Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão: C = P*2.52, sendo C o comprimento em centímetros e P o comprimento em polegadas.
    polegadas = float(input('Informe o comprimento em polegas:'))
    converter = polegadas * 2.52

    print(f'esse comprimento em centímetros é = {converter}')

#Exercicio 17: Leia um valor de comprimento em centímetros e apresente-o convertido em poldegadas.
A fórmula de conversão é: P = C/2.52, sendo C o comprimento em centímetros e P o comprimento em polegadas
    centimetros = float(input('Informe o comprimento em centímetros:'))
    converter = centimetros/2.52

    print(f'esse comprimento em poldegadas é = {converter}')

#Exercicio 18: Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos
    volume = float(input('Informe um volume em metros cúbicos:'))
    converter = 1000 * volume

    print(f'esse volume em litros é = {converter}')

#Exercicio 19: Leia um valor de volume em litros  m³ e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos
    cubicos = float(input('Informe um volume em metros cúbicos:'))
    converter = cubicos/1000

    print(f'esse volume em litros é = {converter}³')

#Exercicio 20: Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
    quilogramas = float(input('Informe um valor de massa em quilogramas:'))
    converter = quilogramas/0.45

    print(f'esse massa convertida em libras, é = {converter}')

#Exercicio 21: Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmulas de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
    libra = float(input('Informe um valor de massa em libras:'))
    converter = libra * 0.45

    print(f'esse massa convertida em quilogramas, é = {converter}')

#Exercicio 22: Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91*J, sendo J o comprimento em jardas e M o comprimento em metros.
    metros = float(input('Informe um valor de comprimento em jardas:'))
    converter = 0.91*metros

    print(f'essa jardas convertida em metros, é = {converter}')

#Exercicio 23: Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é: J = M/0.91, sendo J o comprimento em jardas e M o comprimento em metros.
    jardas = float(input('Informe um valor de comprimento em metros:'))
    converter = jardas/0.91

    print(f'essa jardas convertida em jardas, é = {converter}')

#Exercicio 24: Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M*0.000247, sendo M a área em metros quadrados e A a área em acres.
    area = float(input('Informe um valor de área em metros quadradas em m²:'))
    converter = area*0.000247

    print(f'essa área convertida em acres, é = {converter}')

#Exercicio 25: Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.
    area = float(input('Informe um valor de área em acres:'))
    converter = area*4048.58

    print(f'essa área convertida em metros quadrados, é = {converter}²')

#Exercicio 26: Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M*0.0001, sendo M a área em metros quadrados e A a área em acres.
    area = float(input('Informe um valor de área em metros quadrados m²:'))
    converter = area*0.0001

    print(f'essa área convertida em hectares, é = {converter}')

#Exercicio 27: Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
    area = float(input('Informe o valor da área em hectar:'))
    conversao = area * 10000

    print(f'a conversão da área para metros quadrados é: {conversao}²')

#Exercicio 28: Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
    valor00 = float(input('Primeito valor:'))
    valor01 = float(input('Segundo valor:'))
    valor02 = float(input('Terceiro valor'))
    valor00 = valor00**2
    valor01 = valor01**2
    valor02 = valor02**2
    soma = valor00 + valor01 + valor02

    print(f'Primeiro número = {valor00} \nSegundo valor = {valor01} \nTerceiro valor = {valor02} \nSoma = {soma}')

#Exercicio 29: Leia quatro notas, calcule a média aritmética e imprima o resultado.
    nota00 = float(input('Digite a primeira nota:'))
    nota01 = float(input('Digite a segunda nota:'))
    nota02 = float(input('Digite a terceira nota:'))
    nota03 = float(input('Digite a quarta nota:'))
    media = (nota00 + nota01 + nota02 + nota03) / 4

    print(f'A média é: {media}')

#Exercicio 30: Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
    real = float(input('Informe o seu valor em R$:'))
    dolar = 5.32
    convert = real*dolar

    print(f'O valor é R${real}, hoje o dólar está US{dolar}, e o seu total em dólar é {convert}')

#Exercicio 31: Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
    number = int(input('Informe um número inteiro:'))
    ant = number-1
    suc = number+1

    print(f'O número que você informou é {number}. \nO antecessor é {ant} e o sucessor é {suc}')

#Exercicio 32: Lei um número inteiro e imprima a soma do sucessor de seu tiplo com o antecessor de seu dobro.
    number = int(input('Informe um númeor inteiro:'))
    part1 = (number * 3) + 1
    part2 = (number * 2) - 1
    soma = part1 + part2

    print(f'O número informado é: {number} \n Resultado = {soma}')

#Exercicio 33: Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
    lado = float(input('Informe o lado do quadrado:'))
    area = lado*lado

    print(f'A área total é:{area}²')

#Exercicio 34: Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é PI * raio², considera PI = 3.141592
    raio = float(input('Informe o raio:'))
    pi = 3.141592
    area = pi * raio**2

    print(f'A área do circulo é:{area}')

#Exercicio 35: Sejam A e B os catetos de um triãngulo, onde a hipotenusa é obtida pela equação:
hipotenusa = Raiz(a² + b²). Faça um programa que receba os valores de A e B e calcule o valor da hipotenusa
da equação. Imprimir o resultado dessa operação.
    import math

    a = float(input('Informe o primeiro cateto:'))
    b = float(input('Informe o segundo cateto:'))
    hipotenusa = math.pow(a, 1/2) + math.pow(b, 1/2)

    print(f'A hipotenusa é:{hipotenusa}')

#Exercicio 36: Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um
cilindro circular é calculado por meio da seguinte fórmula: V = PI * raio² * altura, onde PI = 3.141592
    altura = float(input('Informe a altura do cilindro:'))
    raio = float(input('Informe também o raio do cilindro:'))
    pi = 3.141592
    volume = pi * (raio**2) * altura

    print(f'O volume do cilindro é:{volume}')

#Exercicio 37: Faça um programa que leia o valor de um produto e imprima o valor com desconto, tento em vista
que o desconto foi de 12%.
    produto = float(input('Informe o valor do produto:'))
    porcentagem = float(input('Informe a porcetagem do desconto(sem %):'))
    desconto = produto - (produto * porcentagem/100)

    print(f'O valor do produto com desconto ficou:{desconto}')

#Exercicio 38: Leia o sálario de um funcionario. Calcule e imprima o valor do novo salário, sabendo que ele
    recebeu um aumento de 25%
    salario = float(input('Informe o seu salário: R$'))
    aumento = salario + (salario * 25/100)

    print(f'O reajuste do seu salário foi para: R${aumento}')

#Exercicio 39: A importãncia de R$780.000.00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
    - O primeiro ganhador receberá 46%;
    - O segundo receberá 32%;
    - o terceiro recebera o restante;
Calcule e imprima a quantia ganhada por cada um dos vencedores
    premio = 78000000
    primeiro = premio * 46/100
    segundo = premio * 32/100
    terceiro = premio - primeiro - segundo

    print(f'Prémio do primeiro colocado:R${primeiro} \nO segundo ganhará:R${segundo} \nO terceiro ficará com:\
    R${terceiro}')

#Exercicio 40: Uma empresa contrata um encanador a R$30.00 por dia. Faça um programa que solicite o número de dias
trabalhadas pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para
importo de renda.
    dias = int(input('Informe o número de dias trabalhados:'))
    descontados = (30.00 * dias) - ((30.00 * dias) * 8/100)

    print(f'O valor a receber líquido ficará R${descontados}, ja descontando os 8% do imposto de renda')

#Exercicio 41: Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pagos ao funcionário, adicionanado 10% sobre o valor calculado.
    valor = float(input('Informe o valor da hora trabalhadas:R$'))
    hora = float(input('Informe a carga horária do mês:'))
    total = (valor * hora) + ((valor * hora) * 10/100)

    print(f'O valor a ser pago é: R${total}')

#Exercicio 42: Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse
funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
    salariobase = float(input('Informe o seu salário-base:R$'))
    imposto = salariobase - (salariobase * 7/100)
    receber = imposto + (salariobase * 5/100)

    print(f'O seu salário liquido é:R${receber}')

#Exercicio 43: Escreva um programa de ajuda para vendedores. A partir de um valor total lidom mostre:
    - O total a pagar com desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
    - A comissão do vendedos, no caso da venda parcelada(5% sobre o valor total)

    preco = float(input('Informe o valor do produto escolhido:R$'))
    desconto = 10
    parcela = 3
    comissao = 5
    avista = preco - (preco * desconto/100)
    parcelada = preco/parcela
    comissaovista = avista * comissao/100
    comissaoparc = preco * comissao/100

    print(f'O valor a vista:R${avista} \nValor parcelado: {parcela}x de R${parcelada}')
    print(f'A comissão(A vista):R${comissaovista} \nComissão(parcelado):R${comissaoparc}')

#Exercicio 44: Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantors degraus o usuário deverá subir para atingir seu objetivo.
    degrau = float(input('Informe a alturada do degrau:'))
    altura = float(input('Qaul a altura que deseja subir?'))
    obj = altura/degrau

    print(f'Você precisa subir {int(obj)} degraus')

#Exercicio 45: Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASC// para resolver
o problema.
    letra = str(input('Informe uma letra maiúscula para converte para minúscula:'))

    print(letra.lower())

#Exercicio 46: Faça um programa que leia um número inteiro positivo de três digitos(de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
    number = input('Digite um número inteiro com três digitos:')

    print(number[::-1])

#Exercicio 47: Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha
    number = input('Digite um numero inteiro de quatro digitos:')

    print(f'{number[0]} \n{number[1]} \n{number[2]} \n{number[3]} \n')

#Exercicio 48: Leia um valor inteiro em segundo, e imprima-o em horas, minutos, e segundo.
    number = int(input('Informe valor em segundos:'))
    hora = number/3600
    minuto = number/60

    print(f'Hora:{hora} \nMinuto:{minuto} \nSegundos:{number}')

#Exercicio 49: Faça um programa que leia o horário(Hora,minuto e segundo) de inicio e a duração, em segundos,
de uma experiencia biologica. O programa deve resultar com o novo horário(hora, minuto e segundo) do termino da mesma.
    print('Preencha os campos abaixo com o horário atual')

    h = int(input('Hora: '))
    m = int(input('Minuto: '))
    s = int(input('Segundo: '))
    d = int(input('\nDuração do evento (segundos): '))

    s_final = (s + d) % 60
    m_final = (m + (s+d)//60) % 60
    h_final = (h + (m + (s+d)//60)//60) % 24

    print(f'O fim do evento se dará às {h_final}h {m_final}min e {s_final} segundos')

#Exercicio 50: Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano
atual.
    idade = int(input('Informe sua idade:'))
    ano = int(input('Informe o ano atual'))
    data = ano - idade
    print(data)

#Exercicio 51: Esqueva um programa que leias as coordenadas x e y de pontos no R² e calcule a distãncia origem(0,0)
    x = int(input('Informe a primeira coordenada:'))
    y = int(input('Informe a segunda coordenada:'))
    a = (x**2 + y**2)**1/2

    print(a)

#Exercicio 52: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
    amigo01 = input('Amigo 01:')
    valor01 = float(input('Informe o seu investimento:R$'))
    amigo02 = input('Amigo 02:')
    valor02 = float(input('Informe o seu investimento:R$'))
    amigo03 = input('Amigo 03:')
    valor03 = float(input('Informe o seu investimento:R$'))
    premio = float(input('Qual o valor do prêmio:R$'))

    apostatotal = valor01 + valor02 + valor03
    p1 = valor01/apostatotal
    p2 = valor02/apostatotal
    p3 = valor03/apostatotal
    recebe01 = premio * p1
    recebe02 = premio * p2
    recebe03 = premio * p3

    print(f'O {amigo01} recebe {recebe01} \nO {amigo02} recebe {recebe02} \nO {amigo03} recebe {recebe03}')

#Exercicio 53: Faça um programa para ler as dimensões de um terreno(comprimento C e largura L), bem como o preço do
metro de tela P. Imprima o custo para cercar esse mesmo terreno.
    comprimento = float(input('Informe o comprimento do terreno:'))
    largura = float(input('Informe a largura do terrreno:'))
    preco = float(input('Informe o valor do metro da tela:'))

    valor = (comprimento * largura) * preco

    print(f'O custo da tela ficará:R${valor}')

"""

