# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:56:55 2019

@author: pablo gullith
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1 + (1/2)*np.tanh(2*x)

h = 1e-6
x = np.linspace (-2,2,100)
derivadanum = (f(x+h)-2*f(x)+f(x-h))/h**2
derivadareal = (-16*np.sinh(2*x))/(3*np.cosh(2*x)+np.cosh(6*x))

plt.plot(x,derivadanum,label="Derivada Numérica",color='c',marker='o')
plt.plot(x,derivadareal,label="Derivada Analítica",color='k')
plt.legend()
plt.savefig("Figure_2.png")
plt.show()


