from sympy import * #Sympy opções matemáticas
from pylatex import *  #pylatex opções de manipular frações

def cadeiadecimal_para_fracao(cadeiadecimal):  #Isto só funciona para cadeias decimais positivas. As negativas precisam de tirar primeiro o elemento negativo
    posicao_ponto_decimal=cadeiadecimal.find('.')
    ParteInteira=int(cadeiadecimal[:posicao_ponto_decimal])
    ParteDecimal=int(cadeiadecimal[posicao_ponto_decimal+1:])
    quantidade_algaritmos_decimais=len(cadeiadecimal[posicao_ponto_decimal+1:])
    fracao=ParteInteira+Rational(ParteDecimal,10**quantidade_algaritmos_decimais)
    return fracao

def cadeia_para_fracao(cadeia):
    if '/' not in cadeia and '.' not in cadeia: #Neste if, se a cadeia é simplesmente um número transformamos a cadeia em um inteiro.
        fracao =int(cadeia)
    elif '/' in cadeia: #Trata as cadeias da forma a/b (frações)
        denominador_nao_nulo=False#Essa variável controla os casos a/0 pedindo que o usuário insira novamente o denominador
        while denominador_nao_nulo == False:  #Este control pedira para você inserir a/b desde que b=0
            posicao_simbolo_divisao =cadeia.find('/')
            Numerador=int(cadeia[:posicao_simbolo_divisao])
            Denominador=int(cadeia[posicao_simbolo_divisao+1:])
            if Denominador==0:#Aviso no caso você tente ingressar uma fraçaõ com denominador nulo
                print('Fração inválida. Não é possível dividir por zero')
                cadeia=input('Vamos tentar mais uma vez. Insira uma fração no formato a/b: ')
            else: #neste caso tudo deu certo para transformar a cadeia em números e agora vamos usar esses números para criar uma fração
                denominador_nao_nulo =True
        fracao =Rational(Numerador, Denominador)
    elif '.' in cadeia: #Trata as cadeias da forma a.b ou -a.b (decimais)
        if '-' in cadeia:
            fracao=-1*cadeiadecimal_para_fracao(cadeia[1:])
        else:
            fracao=cadeiadecimal_para_fracao(cadeia)
    return fracao

def separar_cadeias_vetores(cadeia): #Este código separa uma cadeia em tantos vetores (ainda em cadeias) contidos na cadeia original
#A cadeia: '(1,2), (3,2), (2,4)' sera vista como as a lista  ['(1,2)' '(3,2)'  e '(2,4)'].
    lista_auxiliar, lista_vetores_separados = [], []
    inicio_do_vetor,final_do_vetor,numero_vetores=0,0,0
    cadeia_auxiliar='' #Esta cadeia vazia ira armazenar os elementos da lista
    for i in range(len(cadeia)):
        if cadeia[i]!=')':
            final_do_vetor+=1 #O contador final tera por valor o número de elementos do início da cadeia até o elemento anterior a ')'
        else:
            for j in range(inicio_do_vetor, inicio_do_vetor+final_do_vetor+1): #Neste for a cadeia armazena o primeiro vetor para transforma-lo em cadeia
                cadeia_auxiliar+=cadeia[j]
            lista_auxiliar.append(cadeia_auxiliar) #adicionamos o primeiro vetor como elemento da lista v
            numero_vetores+=1 #Este contador aumenta cada vez que um elemento é colocado na lista v, ou seja conta o número
            inicio_do_vetor=inicio_do_vetor+final_do_vetor+1 #o contador iniciará no elemento após '('
            final_do_vetor=0 #contador final reinicia
            cadeia_auxiliar='' #A cadeia reinicia
    for i in range(numero_vetores):
        if i==0:
            lista_vetores_separados.append(lista_auxiliar[0]) #A cadeia zero inicia em '(' e finaliza em ')'
        else:
            lista_vetores_separados.append(lista_auxiliar[i][1::]) #Estas cadeias contém uma ',' antes do vetor então aqui retiramos essa ','
    return lista_vetores_separados

def vetorcadeia_para_vetornumerico(vetorcadeia): #Este código toma o vetor tipo str '(1,2,4)' e transforma ele na tupla de componentes numéricas (1,2,4) o que permite operar os elementos como números
    vetorauxiliar=[]
    final_da_componente,inicio_da_componente,numero_componentes=0,1,0 # inicio_do_vetor começa em 1 para eliminar '(' em cada vetor
    cadeia_auxiliar=''
    for i in range(1,len(vetorcadeia)):
        if vetorcadeia[i]!=',' and vetorcadeia[i]!=')': #final_do_vetor aumentará até acabar o primeiro número real ou até acabar os vetores
            final_da_componente+=1
        else:
            for j in  range(inicio_da_componente,inicio_da_componente+final_da_componente): #Toma  o i-esimo vetor dentro da cadeia e transforma ele no i-esimo elemento da lista sendo ainda cadeia
                cadeia_auxiliar+=vetorcadeia[j]
            vetorauxiliar.append(cadeia_auxiliar) #Observe que cada cadeia aqui é numérica mas está no formato str
            numero_componentes+=1 #Este contador aumenta cada vez que você adiciona um elemento à lista
            inicio_da_componente=inicio_da_componente+final_da_componente+1
            final_da_componente=0
            cadeia_auxiliar=''
    return [cadeia_para_fracao(vetorauxiliar[i]) for i in range(numero_componentes)] #A cadeia numérica é transformada em número através da função cadeia_para_fracao






#Esta função pega a cadeia '(1,2,3), (3,2,4)' e transforma em dois vetores numéricos [1,2,3] e [3,2,4]
def atribuir_vetores(cadeia): 
    cadeia=separar_cadeias_vetores(cadeia)
    vetor1=vetorcadeia_para_vetornumerico(cadeia[0])
    vetor2=vetorcadeia_para_vetornumerico(cadeia[1])
    return vetor1, vetor2

#esta função valida que os dois vetores tenham a mesma dimensão. Precisam ser dois para operar
def validar_dimensao_vetores(vetor1, vetor2):
    while len(vetor1) != len(vetor2): 
        print("Erro: Vetores de dimensão diferentes.")
        dois_vetores=False
        while dois_vetores==False: #Este controle valida que o usuário ingresse dois vetores
            cadeia=input('Ingresse dois vetores, da mesma dimensão, separados por vírgula: ')
            if cadeia.count('(') ==2 and cadeia.count(')')==2:
                dois_vetores=True
        vetor1, vetor2=atribuir_vetores(cadeia)
    return vetor1, vetor2





# Os códigos abaixo são operações com vetores
################################################
################################################

def somar_vetores(vetor1, vetor2):
    vetor1, vetor2=validar_dimensao_vetores(vetor1, vetor2)
    return [vetor1[i] + vetor2[i] for i in range(len(vetor1))] # Retorna uma lista onde cada elemento é a soma entre vetor1 e vetor2


def diferenca_vetores(vetor1, vetor2):
    vetor1, vetor2=validar_dimensao_vetores(vetor1, vetor2)
    return [vetor1[i] - vetor2[i] for i in range(len(vetor1))] # Retorna uma lista onde cada elemento é a diferença entre vetor1 e vetor2


def produto_escalar(vetor1, vetor2):
    vetor1, vetor2=validar_dimensao_vetores(vetor1, vetor2)
    return sum(vetor1[i] * vetor2[i] for i in range(len(vetor1))) # Retorna o valor do produto escalar entre vetor1 e vetor2


def multiplicacao_escalar(vetor, escalar):
    return [vetor[i] * escalar for i in range(len(vetor))] # Retorna uma lista onde cada componente do vetor é multiplicado por um escalar


def norma(vetor):
    return sqrt(produto_escalar(vetor, vetor)) # Retorna a norma do vetor 


def vetor_unitario(vetor):
    while norma(vetor) == 0: # Verifica se o vetor é nulo
        print("Erro: Não é possível calcular o vetor unitário de um vetor nulo.")
        cadeia=input('Ingresse o vetor novamente: ')
        vetor=vetorcadeia_para_vetornumerico(cadeia)
    return [vetor[i]/norma(vetor) for i in range(len(vetor))] # Não deveriamos usar Rational, pois não necessariamente o resultado é inteiro. Se der problema, pode ser por isso.
 

def produto_vetorial(vetor1, vetor2):
    while len(vetor1) != 3 or len(vetor2) != 3: # Verifica se os dois vetores são tridimensionais
        print("Erro: Pelo menos um vetor não é tridimensional.")
        cadeia=input('Ingresse dois vetores tridimensionais separados por vírgula: ')
        dimensao_vetor1=separar_cadeias_vetores(cadeia)[0].count(',')+1 # Conta o número de componentes do vetor1
        dimensao_vetor2=separar_cadeias_vetores(cadeia)[1].count(',')+1 # Conta o número de componentes do vetor2
        if dimensao_vetor1 ==3 and dimensao_vetor2==3:
            vetor1, vetor2=atribuir_vetores(cadeia)
    return [vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1],
            vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2],
            vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]]


def projecaovetorial_vetor1_sobre_vetor2(vetor1, vetor2):
    vetor1, vetor2=validar_dimensao_vetores(vetor1, vetor2)
    while norma(vetor2) == 0: # Verifica se o vetor2 é nulo
        print("Erro: Não é possível projetar sobre o vetor nulo.")
        cadeia=input('Ingresse o segundo vetor novamente: ')
        vetor2=vetorcadeia_para_vetornumerico(cadeia)
    numerador_coeficiente=produto_escalar(vetor1, vetor2)
    denominador_coeficiente=produto_escalar(vetor2, vetor2)
    coeficiente=Rational(numerador_coeficiente,denominador_coeficiente)
    return [coeficiente * vetor2[i] for i in range(len(vetor1))]


def componentevetorial_vetor1_sobre_vetor2(vetor1, vetor2):
    vetor1, vetor2=validar_dimensao_vetores(vetor1, vetor2)
    while norma(vetor2) == 0: # Verifica se o vetor2 é nulo
        print("Erro: Não é possível calcular a componente ortogonal em relação ao vetor nulo.")
        cadeia=input('Ingresse o segundo vetor novamente: ')
        vetor2=vetorcadeia_para_vetornumerico(cadeia)
    numerador_componente=produto_escalar(vetor1, vetor2)
    denominador_componente=produto_escalar(vetor2, vetor2)
    componente=Rational(numerador_componente,denominador_componente)
    return abs(componente)


def ortogonalizacao_gram_schmidt(vetores):
    vetores_ortogonais=[]
    for i in range(len(vetores)):
        if i==0:
            vetores_ortogonais.append(vetores[i])
        else:
            auxiliar=[]
            for j in range(i):
                if j==0:
                    auxiliar.append(vetores[i])
                auxiliar.append(diferenca_vetores(auxiliar[j],projecaovetorial_vetor1_sobre_vetor2(vetores[i],vetores_ortogonais[j])))
                if j==i-1:
                    vetores_ortogonais.append(auxiliar[i])
    return vetores_ortogonais










# Operações para apresentar valores na tela

def mostrar_vetores(numero_vetores,vetorescadeia,vetores_dimensoes_diferentes):
    if vetores_dimensoes_diferentes==True:
        print(f'Você inseriu os seguintes {numero_vetores} pontos:')
        for i in range(numero_vetores):
            vetor_numerico=vetorcadeia_para_vetornumerico(vetorescadeia[i])
            print(f'{tuple(vetor_numerico)} é um ponto de {len(vetor_numerico)} componentes')
    else:
        print(f'Você inseriu os seguintes {numero_vetores} pontos de {len(vetorcadeia_para_vetornumerico(vetorescadeia[0]))} componentes:')
        for i in range(numero_vetores):
            vetor_numerico=vetorcadeia_para_vetornumerico(vetorescadeia[i])
            print(tuple(vetor_numerico))