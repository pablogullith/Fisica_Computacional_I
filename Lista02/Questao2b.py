# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:37:35 2019

@author: pablo gullith
"""
#Questão 2b:
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

# Parâmetros físicos
# Comprimento de onda lambda = 500 nm = 0.5 um
# Região no plano focal cobrindo r de 0 até 1 um: coordenadas x e y de -1 a 1 um
wavelength = 0.5  # em micrometros (um)
k = 2 * pi / wavelength

# Malha 2D no plano focal (em micrometros)
# Grade 201x201 para alta resolução e inclusão exata da origem (0, 0)
x, y = np.mgrid[-1:1:201j, -1:1:201j]
r = np.sqrt(x**2 + y**2)

# Intensidade I(r) = (J1(kr) / kr)**2
# Dica 1: lim_{x->0} J1(x)/x = 1/2, logo I(0) = (1/2)**2 = 0.25
kr = k * r
ratio = np.full_like(kr, 0.5)
mask = (kr != 0)
ratio[mask] = J(1, kr[mask]) / kr[mask]
I = ratio**2

# Gráfico de densidade conforme Dica 2: mapa 'hot' e vmax=0.01 para evidenciar os anéis
plt.figure(figsize=(7, 6))
plt.imshow(I, vmax=0.01, extent=(-1, 1, -1, 1), cmap='hot')
plt.title(r"Padrão de Difração Circular (Disco de Airy) - $\lambda = 500\text{ nm}$")
plt.xlabel(r"$x\ (\mu\text{m})$")
plt.ylabel(r"$y\ (\mu\text{m})$")
plt.colorbar(label="Intensidade relativa $I(r)$")
plt.savefig("Figure_3.png", dpi=300, bbox_inches="tight")
plt.show()
