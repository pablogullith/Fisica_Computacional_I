# -*- coding: utf-8 -*-
"""
Created on Thu Feb  28 23:59:45 2019

@author: pablo gullith
"""

#Questão 1:
#Aluno: Pablo Gullith de Melo Dantas
import numpy as n

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))



#a)
print("A)")
delta = n.power(b,2)-(4*a*c)

if delta <= 0:
	print("não há solução")
else:
	x1= ((-b)+n.sqrt(delta))/(2*a)
	x2= ((-b)-n.sqrt(delta))/(2*a)

	print("X1:", x1)
	print("X2:", x2)

#b)
print("B)")
delta = n.power(b,2)-(4*a*c)

if delta <= 0:
	print("não há solução")
else:
	x1= (2*c)/((-b)-n.sqrt(delta))
	x2= (2*c)/((-b)+n.sqrt(delta))

	print("X1:", x1)
	print("X2:", x2)

#c) Observamos que a maior precisão está nos valores em que (-b)-n.sqrt(delta))
# está presente 
print("C)")
if delta <= 0:
	print("não há solução")
else:
	x1= (2*c)/((-b)-n.sqrt(delta))
	x2= ((-b)-n.sqrt(delta))/(2*a)

	print("X1:", x1)
	print("X2:", x2)







