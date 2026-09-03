# -*- coding: utf-8 -*-
"""
Created on Fri Apr  12 20:15:33 2019

@author: pablo gullith
"""

#Bibliotecas
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

#Função
def f(x,c):
    return 1 - np.exp(-c*x)

#Dados usados na questão
Ladox = []
Ladoy = []
Precisao = 1e-6
x1 = 1.0
Erro = 1.0
Interacoes = 0
c = 0
C = 2

#While para dar o valor da equação e a quantidade de interações
while Erro > Precisao:
  x1,x2 = 1 - np.exp(-C*x1), x1
  Erro = abs((x1-x2)/(1-1/(C*np.exp(-C*x1))))
  Interacoes+=1

#Printa o resultado  
print('\nO RESULTADO DESSA EQUAÇÃO É: {} E LEVOU {} INTERAÇÕES.'.format(x1,Interacoes))

#Resultado para nos dar o gráfico 
def Resultado(h,c):
    Sol = 0
    x = 1e-1

   
    while(True):
        Sol = x
        x = f(Sol,c)
        
        if(abs(x - Sol) < h):
            break
        
    return x
  
while(c <= 3):
      Ladox.append(c)
      Ladoy.append(Resultado(1e-6,c))
        
        
      c = c + 0.01

plt.plot(Ladox,Ladoy,'r')
plt.ylabel("$x$")
plt.xlabel("$c$")
plt.savefig("Figure_1.png")
plt.show()   
  