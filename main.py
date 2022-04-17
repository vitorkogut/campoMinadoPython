############################################
# M1 - João Vitor e Nicole
# Linguagem Python
############################################

import numpy as np
from xml.dom.expatbuilder import parseString
from numpy import character, integer, mat
import random as rand

def imprimeBonito(mat,matJogadas, altura, largura): # Imprime o mapa de acordo com o tamanho desejado pelo jogador
    for i in range(altura-1):
        print("")
        for k in range(largura-1):
            if(matJogadas[i,k] == "1"):
                print(mat[i,k], end =" ")
            else:
                print("#", end =" ")

def colocaValores(mat,altura,largura):
    for i in range(altura - 1):
        for k in range(largura - 1):
            if( rand.randint(1,15) == 5): # caso 5 coloca uma bomba
                mat[i,k] = 'X'
            else:
                mat[i,k] = '#'

    for i in range(altura - 1): # Essa funcao checa o posicionamento das bombas adjacentes e mostra quantas tem 
        for k in range(largura - 1):
            if(mat[i,k] != 'X'):
                bombas = 0
                try:
                    if(mat[i-1,k-1] == 'X'): #Ele checa sempre as posições adjacentes
                        bombas = bombas + 1 # E soma um ao contador de bombas
                except:
                    bombas = bombas

                try:
                    if(mat[i-1,k] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i-1,k+1] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i,k-1] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i,k+1] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i+1,k-1] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i+1,k] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas
                
                try:
                    if(mat[i+1,k+1] == 'X'):
                        bombas = bombas + 1
                except:
                    bombas = bombas

                if(bombas > 0):
                    mat[i,k] = bombas
                else:
                    mat[i,k] = "-"

def liberaEspacos(mat,matJogadas, altura, largura): # Essa função checa os espaços vazios adijacentes e libera os mesmos se o campo escolhido for "-"
    for cont in range(altura):
        for i in range(altura-1):
            for k in range(largura-1):
                if(matJogadas[i,k] == "1" and mat[i,k] == "-"): #Se o campo escolhido for "-" a função é feita
                    try:
                        if(mat[i-1,k-1] == '-'):
                            matJogadas[i-1,k-1] = "1"
                    except:
                        i=i

                    try:
                        if(mat[i-1,k] == '-'):
                            matJogadas[i-1,k] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i-1,k+1] == '-'):
                            matJogadas[i-1,k+1] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i,k-1] == '-'):
                            matJogadas[i,k-1] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i,k+1] == '-'):
                            matJogadas[i,k+1] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i+1,k-1] == '-'):
                            matJogadas[i+1,k-1] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i+1,k] == '-'):
                            matJogadas[i+1,k] = "1"
                    except:
                        i=i
                    
                    try:
                        if(mat[i+1,k+1] == '-'):
                            matJogadas[i+1,k+1] = "1"
                    except: 
                        i=i


print("\n###################################### CAMPO MINADO ############################################")
print("\n Deseja iniciar o jogo?")
print("\n 1 - Sim")
print("\n 2 - Não")
print("\n ##############################################################################################")

play = int(input())


while (play==1): #Enquanto o jogador desejar, o jogo reinicia após perder
    largura = 0
    altura = 0

    print(" ####################### CAMPO MINADO! ############################\n\n")
    print("Insira a largura do mapa: ")  # O usuario escolhe os dados do mapa
    largura = int(input())
    print("Insira a altura do mapa: ") 
    altura = int(input())

    largura = largura + 1
    altura = altura + 1

    matP = np.zeros((largura,altura), dtype=str)
    matJogadas = np.zeros((largura,altura), dtype=str)

    colocaValores(matP, altura, largura) #Chama as funçoes de montagem e impressão
    imprimeBonito(matP,matJogadas, altura, largura)

    jogando = True
    while(jogando):

        print("\n\nPara jogar, selecione a posição a ser descoberta: \n")
        print("\nInsira a coluna: ")  #Começa o jogo
        coluna = int(input())
        print("Insira a linha: ")
        linha = int(input()) 

        matJogadas[linha,coluna] = "1"
        liberaEspacos(matP,matJogadas, altura, largura)
        imprimeBonito(matP,matJogadas, altura, largura)

        if(matP[linha,coluna] == "X"):
            print("\n\n ########### VOCE PERDEU! ###########\n")
            print("\n Deseja continuar jogando? 1  - Sim 2 - Não")
            jogando = False
            play = int(input())


   

