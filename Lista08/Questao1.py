# -*- coding: utf-8 -*-
"""
Created on Mon May 13 2019
@author: Pablo Gullith
"""
# Questão 1: Animação de sistema de massas e molas acopladas usando Matplotlib
# Aluno: Pablo Gullith de Melo Dantas
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Garante o carregamento do módulo banded mesmo se executado fora da pasta Lista08

if "__file__" in globals():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
else:

    sys.path.insert(0, os.path.join(os.getcwd(), "Lista08"))
from banded import banded

# Constantes do problema
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2 * k - m * omega**2

# Montagem da matriz tridiagonal (formato banded: 1 acima, 1 abaixo)
A = np.empty([3, N], float)

for i in range(N):
    A[0, i] = -k
    A[1, i] = alpha
    A[2, i] = -k

# Condições de contorno das extremidades
A[1, 0] = alpha - k
A[1, N - 1] = alpha - k

# Vetor de força externa aplicada na primeira massa
v = np.zeros(N, float)
v[0] = C

# Resolução do sistema linear A * x = v para obter as amplitudes x_i
x = banded(A, v, 1, 1)

# Configuração da Animação com Matplotlib
# Posições de repouso das massas (espaçadas por delta = 2 unidades horizontais)

delta = 2.0
pos_eq = (np.arange(N) - N / 2.0) * delta
y = np.zeros(N)

fig, ax = plt.subplots(figsize=(12, 3))
ax.set_xlim(pos_eq[0] - 2.5, pos_eq[-1] + 2.5)
ax.set_ylim(-1.0, 1.0)
ax.set_yticks([])
ax.set_xlabel("Posição horizontal (x)")
ax.set_title(f"Vibração em Cadeia de {N} Massas e Molas Acopladas")
# Marcadores de referência para as posições de equilíbrio/repouso
ax.plot(pos_eq, y, '|', color='silver', markersize=18, label="Posições de repouso")

# Linha conectando as massas (representando as molas)
linha_molas, = ax.plot([], [], '-', color='gray', lw=1.5)

# Círculos representando as massas individuais (esferas)

massas, = ax.plot([], [], 'o', color='royalblue', markersize=10,
                  markeredgecolor='black', label="Massas (esferas)")



ax.legend(loc="upper right", framealpha=0.9)

# Função de inicialização da animação

def init():
    linha_molas.set_data(pos_eq, y)
    massas.set_data(pos_eq, y)
    return linha_molas, massas

# Função de atualização a cada quadro

# Deslocamento relativo u_i(t) = Re(x_i * e^(i * omega * t)) = x_i * cos(omega * t)
dt = 0.05

def update(frame):
    t = frame * dt
    pos = pos_eq + x * np.cos(omega * t)
    linha_molas.set_data(pos, y)
    massas.set_data(pos, y)
    return linha_molas, massas



# Animação contínua (interval=50 ms -> 20 quadros por segundo)
ani = animation.FuncAnimation(fig, update, init_func=init, interval=50, blit=True, cache_frame_data=False)
plt.tight_layout()
plt.show()