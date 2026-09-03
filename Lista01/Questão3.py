# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:41:08 2019

@author: pablo gullith
"""
#Questão 3:
#Aluno: Pablo Gullith de Melo Dantas
import os
import numpy as n
import matplotlib.pyplot as p

# Obtém o caminho do arquivo de forma compatível com qualquer forma de execução
if "__file__" in globals():
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "velocities.txt")
else:
    caminho = "velocities.txt"

if not os.path.exists(caminho):
    caminho = os.path.join("Lista01", "velocities.txt")

dados = n.loadtxt(caminho) 

t = dados[:,0] #tempo 
v = dados[:,1] #velocidade 

# Regra do Trapézio: cálculo da distância percorrida s(t) em função do tempo
# No tempo t = 0, a distância é 0. Em cada intervalo [t_i, t_{i+1}], delta_s = (h/2)*(v_i + v_{i+1})
s = [0.0]
area = 0.0

for i in range(len(v) - 1):
	h = t[i+1] - t[i]
	area += (h / 2) * (v[i] + v[i+1])
	s.append(area)

s = n.array(s)

print("Distância total:", area)
print("Tamanho de s:", len(s))
print("Tamanho de t:", len(t))


p.subplot(2,1,1)
p.plot(t,v)
p.xlabel("Tempo (s)")
p.ylabel("Velocidade (m/s)")
p.xlim(n.min(t),n.max(t))

p.subplot(2,1,2)
p.plot(t,s)
p.ylabel("Distância (m)")
p.xlabel("Tempo (s)")
p.xlim(n.min(t),n.max(t))
p.tight_layout()
p.savefig("Figura_1.png")
p.show()
