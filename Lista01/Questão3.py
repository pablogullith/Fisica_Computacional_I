# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:41:08 2019

@author: pablo gullith
"""
#Questão 3:
#Aluno: Pablo Gullith de Melo Dantas
import numpy as n
import matplotlib.pyplot as p

area = 0
s    = []
dados = n.loadtxt("velocities.txt") 

t = dados[:,0] #tempo 
v = dados[:,1] #velocidade 

for i in range(len(v)):
	if v[i] != v[-1]:
			
		area += v[i]+v[i+1]
	s.append(area/2) 
		
print(area/2)
s = n.array(s)
print(len(s))
print(len(t))


p.subplot(2,1,1)
p.plot(t,v)
p.xlabel("Tempo")
p.ylabel("Velocidade")
p.xlim(n.min(t),n.max(t))
p.subplot(2,1,2)
p.plot(t,s)
p.ylabel("Área")
p.xlabel("Tempo")
p.xlim(n.min(t),n.max(t))
p.show()
