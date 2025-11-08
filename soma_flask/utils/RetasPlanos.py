from utils.bibliotecaswm import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
# Evitaremos que o usuário insira vetores com denominador zero
#ou que insira vetores de dimensões diferentes
vetores_dimensoes_diferentes=True
Dividir_por_zero=True
while vetores_dimensoes_diferentes==True or Dividir_por_zero==True:
    cadeia=input('Insira os pontos na reta ou no plano separados por vírgula:')
    cadeia=cadeia.replace(' ', '') #Tiramos os espaços em branco desnecessários
    if '/0,' not in cadeia and '/0)' not in cadeia:
        Dividir_por_zero=False
    if Dividir_por_zero==False:
        numero_vetores=cadeia.count(')') #Contamos quantos vetores o usuário inseriu
        if numero_vetores<2: #or numero_vetores>3:
            print('Erro: Para calcular a equação de uma reta insira dois pontos e para calcular a equação de um plano insira três pontos. Vamos tentar novamente.')
            vetores_dimensoes_diferentes=True
            Dividir_por_zero=True
        else:
            vetorescadeia=separar_cadeias_vetores(cadeia)
            dimensao_vetor1=vetorescadeia[0].count(',')+1 #Contamos a dimensão do primeiro vetor
            for i in range(1,numero_vetores):
                dimensao_vetor_i=vetorescadeia[i].count(',')+1
                if dimensao_vetor1!=dimensao_vetor_i:
                    vetores_dimensoes_diferentes=True
                    Dividir_por_zero=True
                else:
                    vetores_dimensoes_diferentes=False
            if vetores_dimensoes_diferentes==True:
                mostrar_vetores(numero_vetores,vetorescadeia,vetores_dimensoes_diferentes)
                print('Não é possível operar pontos(vetores) de dimensões diferentes. Vamos tentar novamente.')
            else:
                mostrar_vetores(numero_vetores,vetorescadeia,vetores_dimensoes_diferentes)

#Aqui temos garantido ter dois ou três vetores de mesma dimensão e sem divisão por zero
#Agora vamos calcular a equação da reta ou do plano. 

if numero_vetores==2: #Neste caso podemos calcular a equação da reta sendo ela em duas ou três dimensões.
    vetoresnumericos=[]
    for i in range(0,numero_vetores):
        vetor_numerico=vetorcadeia_para_vetornumerico(vetorescadeia[i])
        vetoresnumericos.append(vetor_numerico)     
    if vetoresnumericos[0]==vetoresnumericos[1]:
        print('Você tem um único ponto.')
    elif dimensao_vetor1==1:
        print('Você está na reta real.')
    elif dimensao_vetor1==2:
        vetordiretor=diferenca_vetores(vetoresnumericos[1],vetoresnumericos[0])
        print('A equação vetorial da reta que passa pelos pontos dados é:')
        print(f'L:(x,y)={tuple(vetoresnumericos[0])}+t{tuple(vetordiretor)}')
        print('As equações paramétricas da reta são:')
        t = Symbol('t') 
        print(f'x={vetoresnumericos[0][0]+1*vetordiretor[0]*t}')
        print(f'y={vetoresnumericos[0][1]+1*vetordiretor[1]*t}')
        x=Symbol('x')
        y=Symbol('y')
        #Agora vamos calcular a equação geral da reta
        vetornormal=[-vetordiretor[1],vetordiretor[0]] #as componentes deste vetor são a e b na equação ax+by=c
        c=produto_escalar(vetornormal,vetoresnumericos[0])# este valor es para calcular el termino c da ax+by=c
        print(f'O vetor diretor à reta é v={tuple(vetoresnumericos[1])}- {tuple(vetoresnumericos[0])}={tuple(vetordiretor)}')
        print(f'O vetor normal à reta é n={tuple(vetornormal)}')
        print('Portanto, a equação da reta é:')
        print(f'{vetornormal[0]*x + vetornormal[1]*y} = c')
        print(f'onde c={tuple(vetornormal)}.{tuple(vetoresnumericos[0])}={c}')

        if vetornormal[0]<0:#Isto somente é visual para ter x com sinal positivo.
            print('Em consequência, a equação geral da reta que passa pelos pontos dados é: ',end='')
            print(f'{-1*vetornormal[0]*x-1*vetornormal[1]*y}={-c}')
        else: #mesma coisa, visual
            print('Em consequência, a equação geral da reta que passa pelos pontos dados é: ',end='')
            print(f'{vetornormal[0]*x+vetornormal[1]*y}={c}')
    elif dimensao_vetor1==3:
        vetordiretor=diferenca_vetores(vetoresnumericos[1],vetoresnumericos[0])
        print('A equação vetorial da reta espacial que passa pelos pontos dados é:')
        print(f'L:(x,y,z)={tuple(vetoresnumericos[0])}+t{tuple(vetordiretor)}')
if numero_vetores==3: #Neste caso podemos calcular a equação do plano sendo ele em três dimensões.
    vetoresnumericos=[]
    for i in range(0,numero_vetores):
        vetor_numerico=vetorcadeia_para_vetornumerico(vetorescadeia[i])
        vetoresnumericos.append(vetor_numerico)
    vetor_contido1=diferenca_vetores(vetoresnumericos[0],vetoresnumericos[1])#Dados os pontos b0 e b1 criamos o vetor v1 contido no plano
    vetor_contido2=diferenca_vetores(vetoresnumericos[0],vetoresnumericos[2])#Dados os pontos b0 e b1 criamos o vetor v2 contido no plano
    vetornormal=produto_vetorial(vetor_contido1,vetor_contido2) #vetornormal é o vetor normal ou seja o produto vetorial de v1 e v2
    d=produto_escalar(vetornormal,vetoresnumericos[0])#A equação do plano é (p-p0).n=0 separando p.n é o lado algébrico e n.b0 é d na equação ax+by+cz=d
    x=Symbol('x')#permite trabalhar com variável x análogo para as outras variáveis
    y=Symbol('y')
    z=Symbol('z')
    if vetornormal==[0,0,0]:
        print('Os três pontos inseridos são colineares e portanto não definem um plano.')
    else:
        print('Dois vetores contidos no plano são: ')
        print(f'V={tuple(vetor_contido1)}={tuple(vetoresnumericos[0])}-{tuple(vetoresnumericos[1])}')
        print(f'W={tuple(vetor_contido2)}={tuple(vetoresnumericos[0])}-{tuple(vetoresnumericos[2])}')
        print('Daí, o vetor normal ao plano é:')
        print(f'N = V x W = {tuple(vetor_contido1)}x{tuple(vetor_contido2)}={tuple(vetornormal)}')
        print('Portanto a equação do nosso plano é: ')
        print(f'{1*vetornormal[0]*x + 1*vetornormal[1]*y + 1*vetornormal[2]*z} = d')
        print(f'onde d={tuple(vetornormal)}.{tuple(vetoresnumericos[0])}={d}')
        if vetornormal[0]<0:#parte estética mesmo que no caso da reta anterior
            print('Em consequência, a equação do plano que passa pelos pontos dados é: ',end='')
            print(f'{-1*vetornormal[0]*x -1*vetornormal[1]*y -1*vetornormal[2]*z} = {-d}')
        else:
            print('Em consequência, a equação do plano que passa pelos pontos dados é: ',end='')
            print(f'{vetornormal[0]*x + vetornormal[1]*y + vetornormal[2]*z} = {d}')




# Esta parte não é necessária para um primeiro momento, pode ser desconsiderada.
#Existem evidentes problemas a serem resolvidos na parte abaixo. 
#Precisa validar que os vetores sejam linearmente independentes.
#Não necessariamente o número de vetores é igual à dimensão. É suficiente ter um número de vetores não maior que a dimensão dos mesmos.

if numero_vetores==dimensao_vetor1 and vetores_dimensoes_diferentes==False:
    ortogonalizados=ortogonalizacao_gram_schmidt([vetorcadeia_para_vetornumerico(vetorescadeia[i]) for i in range(numero_vetores)])
    print('Os vetores obtidos no processo de ortogonalização de Gram-Schmidt são:')
    for i in range(numero_vetores):
        if norma(ortogonalizados[i])!=0:
            print(tuple(vetor_unitario(ortogonalizados[i])))
        if norma(ortogonalizados[i])==0:
            print(tuple(ortogonalizados[i]))


