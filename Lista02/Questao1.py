# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:00:00 2019

@author: pablo gullith
"""
#Questão 1:
#Aluno: Pablo Gullith de Melo Dantas
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t**2)

# Regra do trapézio para calcular a integral definida
def integrate(f, a, b, N=100):
    if a == b:
        return 0.0
    h = (b - a) / N
    s = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, N):
        s += f(a + k * h)
    return h * s

# Função E(x) = integral de 0 a x de exp(-t^2) dt
def E(x, N=100):
    return integrate(f, 0, x, N)

# Item a) Calcular E(x) para valores de x entre 0 e 3, usando um passo de 0.1
x_vals = np.arange(0.0, 3.1, 0.1)
E_vals = []

print("=== Item a) Valores de E(x) para x de 0 a 3 (passo 0.1) ===")
print("{:>5} | {:>12}".format("x", "E(x)"))
print("-" * 20)
for xi in x_vals:
    val = E(xi, N=100)
    E_vals.append(val)
    print("{:5.1f} | {:12.8f}".format(xi, val))

# Item b) Gráfico de E(x) em função de x
x_curva = np.linspace(0.0, 3.0, 200)
E_curva = [E(xi, N=100) for xi in x_curva]

plt.figure(figsize=(8, 5))
plt.title(r"Gráfico de $E(x) = \int_0^x e^{-t^2} dt$")
plt.plot(x_curva, E_curva, 'b-', label="$E(x)$")
plt.plot(x_vals, E_vals, 'ro', markersize=4, label="Pontos calculados (passo 0.1)")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.grid(True)
plt.legend()
plt.show()
