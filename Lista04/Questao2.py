# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:48:21 2019

@author: pablo gullith
"""
#Comentários
"""O melhor valor de h para ordem 1 é 1e-6, o melhor valor de h para ordem 3 é
1e-4. Quando calculamos o erro, temos em vista que o computador calcula o erro
de arredondamento somado ao erro de aproximação; sabemos que a derivada de 
ordem 3 nos dá um erro de aproximação de ordem alta h^4, com isso é sábio 
escolher um valor de h mais alto porque este nos dará uma excelente aproximação
e um pequeno erro de arredondamento."""

import matplotlib.pyplot as plt
import numpy as np

#definição da função
def f(x):
    return 1 + (1/2)*np.tanh(2*x)

#definição da derivada centrada
def df(x,h):
    return (f(x + h/2) - f(x - h/2))/h

#definição da derivada analitica
def a(x):
    return -np.tanh(2*x)**2 + 1  

#definição da derivada O3
def df_Ordem3(x,h): 
    return (f(x - 3*h/2) - 27*f(x - h/2) + 27*f(x + h/2) - f(x + 3*h/2))/(24*h)  

#valores de x e h
x = np.linspace(-2,2,100)
h = 1e-4    

#definições para o plot do graph
dO3 = df_Ordem3(x,h) 
da = a(x)               
plt.plot(x,dO3,color="c",marker='o',label="Derivada Numérica Ordem3")
plt.plot(x,da,label="Derivada Analítica",color='k')
plt.legend()
plt.show()

#B e C
H = np.empty(6)
h = 1e-2

for i in range(6):
    H[i] = h
    h = h/10

derivadaO1 = df(0,H) # O1   
derivadaO3 = df_Ordem3(0,H) # O3
ErrosO1 = derivadaO1 - a(0)*np.ones(6) # Error ordem 3
ErrosO3 = derivadaO3 - a(0)*np.ones(6) # Error ordem 3


print("\n\nVALORES DADOS PARA h:",H)
print("\nDERIVADAS DE ORDEM 1 *** ERROS DE ORDEM 1\n")
for i in range(np.size(derivadaO1)):
    print(" ",derivadaO1[i],"   ",ErrosO1[i])

print("\nDERIVADAS DE ORDEM 3 *** ERROS DE ORDEM 3\n")
for i in range(np.size(derivadaO3)):
    print(" ",derivadaO3[i],"   ",ErrosO3[i])  

     

