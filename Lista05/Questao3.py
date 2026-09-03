# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:16:1 2019

@author: pablo gullith
"""
#Bibliotecas
import numpy as np

#Temos que resolver a equação dada usando a busca binária.
Precisao=1e-6

#Definir função 
def f(x):
    return 5*np.exp(-x)+x-5

def Raiz(f,x1,x2,Precisao):
   
    def Ponto_Medio(x,y):
        return (x+y)/2

    def Teste_Sinais(x,y):
        if x<0 and y<0 or x>0 and y>0:
            return True
        else:
            return False

    
    while abs(x1-x2)>Precisao:
        x=Ponto_Medio(x1,x2)
        if Teste_Sinais(f(x1),f(x)):
            x1=x
        elif Teste_Sinais(f(x),f(x2)):
            x2=x
        elif abs(x)<Precisao:
            return x

    return Ponto_Medio(x1,x2)

print('Equação Resolvida é igual a:',Raiz(f,4,6,Precisao))

#Definições para constante de wien e temperatura do sol
XequacaoLinear=Raiz(f,4,6,Precisao)
Velocidadedaluz=299792458
ConstantePlanck=6.62607004*1e-34
ConstanteBoltzmann=1.38064852*1e-23
LambdaSol=502*1e-9 #Pico no comprimento de onda da radiacão emitida pelo Sol.
b=(ConstantePlanck*Velocidadedaluz)/(ConstanteBoltzmann*XequacaoLinear)
T=b/LambdaSol

print('Valor da constante de deslocamento:',b)
print('Temperatura do sol é:',T)