# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:30:09 2019

@author: pablo gullith
"""
#Questão 2a:
#Aluno: Pablo Gullith de Melo Dantas
from __future__ import division, print_function
import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt

def J(m, x, N=1000):
    """
    Calcula a função de Bessel J_m(x) usando a regra de Simpson com N fatias.
    J_m(x) = (1/pi) * integral_0^pi cos(m*theta - x*sin(theta)) dtheta
    """
    x = np.asarray(x)
    
    def f(theta):
        return cos(m * theta - x * sin(theta))
    
    a = 0.0
    b = pi
    h = (b - a) / N
    
    # Regra de Simpson com N fatias (N par)
    s = f(a) + f(b)
    for k in range(1, N, 2):       # Termos ímpares (peso 4)
        s += 4.0 * f(a + k * h)
    for k in range(2, N, 2):       # Termos pares (peso 2)
        s += 2.0 * f(a + k * h)
    
    I = (h / 3.0) * s / pi
    return I

# Intervalo de x de 0 a 20 (usando 200 pontos para uma curva suave)
x = np.linspace(0, 20, 200)

plt.figure(figsize=(9, 5))
plt.title("Funções de Bessel $J_0(x)$, $J_1(x)$ e $J_2(x)$")
plt.plot(x, J(0, x), label=r"$J_0(x)$")
plt.plot(x, J(1, x), label=r"$J_1(x)$")
plt.plot(x, J(2, x), label=r"$J_2(x)$")
plt.axhline(0, color="black", linestyle="--", linewidth=0.7)
plt.xlabel("x")
plt.ylabel(r"$J_m(x)$")
plt.grid(True)
plt.legend()
plt.savefig("Figure_2.png", dpi=300, bbox_inches="tight")
plt.show()
