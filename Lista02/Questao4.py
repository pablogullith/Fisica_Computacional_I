# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:50:39 2019

@author: pablo gullith
"""
#Questao 4:
#Aluno: Pablo Gullith de Melo Dantas
#Biblioteca
import numpy as np

#Definir função
def f(x):
    return np.sin(np.sqrt(100*x))**2
#Método do trapézio
def trapezoidal(a,b,N):
    h = (b-a)/N
    s = (f(a) + f(b))/2
    for i in range(1,N):
        s = s + f(a + i*h)
    return(h*s) 
#Método do trapézio adaptado
def adap_trapezoidal(a,b,N,I_old):
    h = (b-a)/N
    s = 0
    for i in range(1,N,2):
        s = s +  f(a + i*h)
    I_new = h*s + I_old/2
    erroint = (I_new - I_old)/3
    return(I_new,erroint)
a = 0
b = 1
N = 1
I_old = trapezoidal(a,b,N)
erroint = 100
epsilon = 1e-6
while(abs(erroint) > epsilon):
    N = 2*N #O valor de N dobra 
    I_new,erroint = adap_trapezoidal(a,b,N,I_old)
    I_old = I_new
    print('\n-NÚMERO DE FÁTIAS:',N)
    print('-INTEGRAL:',I_new)
    print('-ERRO:',erroint)
    
#O MÉTODO DE WERNER ROMBERG     
print('\n\n-Triângulo de Werner Romberg: \n')  

n = 10    
W = np.zeros((n,n),float)

def WernerRomberg(i,m):
    if(m == 1):
        N = 2**(i-1)
        erroint = (W[i,1] - W[i-1,1])/3
        return(trapezoidal(a,b,N),erroint)
    else:
        erroint = (1/(4**(m-1)-1))*(W[i,m-1]-W[i-1,m-1])
        return(W[i,m-1] + erroint, erroint)

W[1,1],erroint = WernerRomberg(1,1)
erroint = 100
i = 2
print(W[1,1])

while(abs(erroint) > epsilon):
    for m in range(1,i+1):
        W[i,m],erroint = WernerRomberg(i,m)
        print(W[i,m],end="|")
    i = i + 1
    print()   
        
  

    