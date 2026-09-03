# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:10:33 2019

@author: pablo gullith
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1 + (1/2)*np.tanh(2*x)

h = 1e-6
x = np.linspace (-2,2,100)
derivadanum = (f(x+h/2)-f(x-h/2))/h
derivadareal = -np.tanh(2*x)**2 + 1

plt.plot(x,derivadanum,label="Derivada Numérica",color='c',marker='o')
plt.plot(x,derivadareal,label="Derivada Analítica",color='k')
plt.legend()
plt.savefig("Figure_1.png")
plt.show()



