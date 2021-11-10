
# Tipo_Númerico

"""
int -> Inteiro = int(5/2) or 5 // 2
Resto -> 5 % 2 = 1 (Ele mostra o resto que sobre da divisão)
                   (Todo resto de um número inpar = 1 and numero par=0)
"""

# Tipo_Float

"""
Tipo Float -> Número décimal = float(10/5) = 2.0 (Retorna um número décimal)
     
    #A separação das casas decimais é com PONTO e não VÍRGULA.)

Número Complexo = 5j (Conseguimos trabalhar com números complexos acrescentando o J)

Podemos fazer uma dupla atribuição:
<var>, <var1> = 1, 5 (Ou seja, <var> = 1 and <var1> = 5
"""

# Tipo_Booleano

"""
Temos dentro desse tipo duas constantes; True = VERDADEIRO and False = FALSO;
    OBS: Precisamos sempre utilizar a inicial MAIÚSCULA;                                       

Operações Básicas:
    
    #Negação (not):
     - Se o valor booleano for verdadeiro o resultado será falso;
     - Se o valor booleano for falso o resultado será verdadeiro;
     
     ativo = True               ativo = False
     print(not ativo)           print(not ativo)
     False                      True
    
    #Ou (or):
     - É uma operação binária, ou seja, se uma das atribuições for verdadeira ele vai aceitar;
     
     True and True -> True
     True and False -> True
     False and True -> True
     False and False -> False
     
     #E (and):
     - É uma operação binária, mas que precisa que as duas atribuições estejam válidas;
     
     True and True -> True
     True and False -> False
     False and True -> False
     False and False -> True
     
"""

# Tipo_String

"""

Em python, um dado é considerado string sempre que:
- Estiver entre aspas; ('536', 'Maneta', "Vasoura", "5663")
 - Todos os dados que entrar no input;

    name = 'Vitor \nKruel'        #\n pula uma linha
    print(name)
    print(type(name))
    print(name[::-1]) #Começe no primeiro elemento, vá até o ultimo elemento e inverta
    print(name.replace('V', 'P') #Subistitui o 'V' na variável em 'P'
Outras funções:

    - .upper() #Tudo maiúsculo;
    - .lower() #Tudo minúsculo;
    - .title() #Deixa a primeira letra maiúscula;
    - .split() #Deixa a varável em uma lista de string;
       print(name.split()[0]) #Pega o primeiro item da lista; 
    - .replace(x, y) #Ele subistitui x=string em y=string   
"""

# Escopo de Variáveis

"""
/  ESCOPO E O LIMITE QUE EXISTE EM UM LOCAL  /

Dois casos de escopo:

    1- Variáveis globais: São reconhecidas, ou seja, seu escopo comprreende, todo o programa;
        name = 42 #Variáveis globais
    
    2- Variáveis locais:  São reconhecidas apenas na caixa onde foram declaradas;
        if number > 12:
            novo =  numero+10 #Variáveis locais
             
Declaração da variável:

<VARIAVEL> = <VALOR_DA_VALIAVEL>

"""


