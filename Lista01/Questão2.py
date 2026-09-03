# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:09:29 2019

@author: pablo gullith
"""
#Questão 2:
#Aluno: Pablo Gullith de Melo Dantas
x = 1
h = [10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)]

def f(u):
	return u*(u-1)
for i in range(len(h)):
    print("Com h : {} = {}".format(h[i],(f(x + h[i]) - f(x))/h[i]))
    
#a) Não concordam pois uma é feita de maneira análitica usando uma fórmula
#matemática; Já o método computacional usa aproximações.    
#b) Percebe-se que quanto menor o valor do h a precisão será maior, mas quando
#chegamos ao limite de divisão de um float o erro volta a aumentar.    

    
