import numpy as np
from xml.dom.expatbuilder import parseString
from numpy import character, integer, mat
import random as rand

def imprimeBonito(mat,matJogadas, altura, largura):
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

    for i in range(altura - 1):
        for k in range(largura - 1):
            if(mat[i,k] != 'X'):
                bombas = 0
                try:
                    if(mat[i-1,k-1] == 'X'):
                        bombas = bombas + 1
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

def liberaEspacos(mat,matJogadas, altura, largura): 
    for cont in range(altura):
        for i in range(altura-1):
            for k in range(largura-1):
                if(matJogadas[i,k] == "1" and mat[i,k] == "-"):
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


largura = 0
altura = 0

print("CAMPO MINADO!\n\n")
print("Insira a largura do campo: ")
largura = int(input())
print("Insira a altura do campo: ") 
altura = int(input())

largura = largura + 1
altura = altura + 1

matP = np.zeros((largura,altura), dtype=str)
matJogadas = np.zeros((largura,altura), dtype=str)

colocaValores(matP, altura, largura)
imprimeBonito(matP,matJogadas, altura, largura)

jogando = True
while(jogando):
    print("\nInsira a coluna: ")
    coluna = int(input())
    print("Insira a linha: ")
    linha = int(input()) 

    matJogadas[linha,coluna] = "1"
    liberaEspacos(matP,matJogadas, altura, largura)
    imprimeBonito(matP,matJogadas, altura, largura)

    if(matP[linha,coluna] == "X"):
        print("\n\n ########### VOCE PERDEU! ###########")
        jogando = False


   

