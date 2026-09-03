# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:10:33 2019

@author: pablo gullith
"""
#Bibliotecas
import numpy as np

#Variáveis e precisão
a=1
b=2
Precisao=1e-6

#Usaremos aqui o método da relaxação 
def f1(x,y):
    return y*(a+x**2)

def g1(x,y):
    return b/(a+x**2)

def f2(x,y):
    return np.sqrt(b/y-a)

def g2(x,y):
    return x/(a+x**2)

def Pontos_Estacionarios(f,g):    
    Iteracoes=1

    def Mudanca_Relativa(x1,x2):
        return (x1-x2)/x1

    #Os valores iniciais
    x1 = 0.5
    y1 = 0.25
    x2 = f(x1,y1)
    y2 = g(x1,y1)

    while abs(Mudanca_Relativa(x1,x2))>Precisao and abs(Mudanca_Relativa(y1,y2))>Precisao:

        x1,x2,y1,y2=x2,f(x2,y2),y2,g(x2,y2)
        Iteracoes +=1
    print('\nIterações feitas durante o código:',Iteracoes)
    return [x2,y2]

print('\nValores achados:',Pontos_Estacionarios(f2,g2))

#Alguns comentários
"""Se nós usarmos x=f1(x,y) e y=g1(x,y) para resolver os pontos estacionários, veremos que o método do relaxamento irá 
falhar. Porém, se usarmos f2 e g2 mostrados no começo desse algoritmo que são rearranjos das equações reais o método irá
de fato convergir"""
