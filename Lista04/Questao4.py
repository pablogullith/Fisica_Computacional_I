# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:10:33 2019

@author: pablo gullith
"""

import numpy as np
import matplotlib.pyplot as plt

# Permissividade do vácuo e constante eletrostática
eps0 = 8.854187817e-12  # C^2 / (N * m^2)
k_e = 1.0 / (4.0 * np.pi * eps0)  # N * m^2 / C^2 (~ 8.99e9)

# Cargas pontuais de +/- 1 C separadas por 10 cm (0.10 m)
q1 = 1.0   # +1 C
q2 = -1.0  # -1 C

# Posições das cargas (centralizadas na origem ao longo do eixo x)
x1, y1 = 0.05, 0.0   # Carga positiva em +5 cm (0.05 m)
x2, y2 = -0.05, 0.0  # Carga negativa em -5 cm (-0.05 m)


h = 0.01  # Espaçamento da grade: 1 cm = 0.01 m
# Coordenadas variando de -0.5 m a +0.5 m (101 pontos em cada eixo)
x = np.arange(-0.5, 0.5 + h/2, h)
y = np.arange(-0.5, 0.5 + h/2, h)
X, Y = np.meshgrid(x, y)


# Distâncias de cada ponto da grade até as cargas
r1 = np.sqrt((X - x1)**2 + (Y - y1)**2)
r2 = np.sqrt((X - x2)**2 + (Y - y2)**2)

# Proteção para evitar divisão por zero no ponto exato das cargas pontuais
r1[r1 == 0] = 1e-15
r2[r2 == 0] = 1e-15

# Potencial elétrico total pela superposição
phi = k_e * (q1 / r1 + q2 / r2)

# Item (b): Componentes do Campo Elétrico E = -grad(phi)
# Derivadas parciais usando diferenças centradas: Ex = -d(phi)/dx e Ey = -d(phi)/dy
# np.gradient calcula derivadas numéricas usando diferenças centradas no interior
# No meshgrid padrão, o eixo 0 (linhas) corresponde a y e o eixo 1 (colunas) a x
dphi_dy, dphi_dx = np.gradient(phi, h, h)
Ex = -dphi_dx
Ey = -dphi_dy

# Magnitude e direção do campo elétrico
E_mag = np.sqrt(Ex**2 + Ey**2)
E_dir = np.arctan2(Ey, Ex)  # Ângulo da direção em radianos [-pi, pi]


# Visualizações


# --- Figura 1: Potencial Elétrico (Item a) ---
plt.figure(figsize=(7, 6))
# vmin e vmax limitam a escala de cores para evitar saturação devido às singularidades
im_phi = plt.imshow(phi, extent=[-50, 50, -50, 50], origin='lower',
                    cmap='RdBu_r', vmin=-1e11, vmax=1e11)
plt.colorbar(im_phi, label=r'Potencial Elétrico $\phi$ (V)')
plt.plot(x1 * 100, y1 * 100, 'ro', markersize=8, label=r'Carga $+1\text{ C}$')
plt.plot(x2 * 100, y2 * 100, 'bo', markersize=8, label=r'Carga $-1\text{ C}$')
plt.title(r'Potencial Elétrico $\phi(x, y)$ de um Dipolo')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("Figure_potencial.png", dpi=150)

# --- Figura 2: Magnitude e Direção do Campo Elétrico (Item b) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Gráfico de densidade da Magnitude do campo elétrico
im_mag = ax1.imshow(E_mag, extent=[-50, 50, -50, 50], origin='lower',
                    cmap='viridis', vmax=1e13)
ax1.plot(x1 * 100, y1 * 100, 'ro', markersize=6, label=r'$+1\text{ C}$')
ax1.plot(x2 * 100, y2 * 100, 'bo', markersize=6, label=r'$-1\text{ C}$')
ax1.set_title(r'Magnitude do Campo Elétrico $|\vec{E}|$')
ax1.set_xlabel('x (cm)')
ax1.set_ylabel('y (cm)')
ax1.legend(loc='upper right')
fig.colorbar(im_mag, ax=ax1, label=r'Magnitude $|\vec{E}|$ (V/m)')

# 2. Gráfico de densidade da Direção usando o esquema 'hsv' (arco-íris cíclico)
im_dir = ax2.imshow(E_dir, extent=[-50, 50, -50, 50], origin='lower',
                    cmap='hsv', vmin=-np.pi, vmax=np.pi)
ax2.plot(x1 * 100, y1 * 100, 'ko', markersize=6, label='Cargas')
ax2.plot(x2 * 100, y2 * 100, 'ko', markersize=6)
ax2.set_title(r"Direção do Campo Elétrico (Esquema 'hsv')")
ax2.set_xlabel('x (cm)')
ax2.set_ylabel('y (cm)')
ax2.legend(loc='upper right')
cbar_dir = fig.colorbar(im_dir, ax=ax2, label=r'Ângulo $\theta$ (radianos)')
cbar_dir.set_ticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
cbar_dir.set_ticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

plt.tight_layout()
plt.savefig("Figure_campo_densidade.png", dpi=150)

# --- Figura 3: Representação Vetorial com Grade de Flechas (Quiver) ---
plt.figure(figsize=(7, 6))
# Subamostragem da grade para visualização nítida das flechas
skip = 4
Ex_sub = Ex[::skip, ::skip]
Ey_sub = Ey[::skip, ::skip]
# Vetores unitários para representar direção e sentido de forma uniforme
E_sub_mag = np.hypot(Ex_sub, Ey_sub)
E_sub_mag[E_sub_mag == 0] = 1.0
u = Ex_sub / E_sub_mag
v = Ey_sub / E_sub_mag

plt.quiver(X[::skip, ::skip] * 100, Y[::skip, ::skip] * 100, u, v,
           pivot='mid', color='navy', scale=30)
plt.plot(x1 * 100, y1 * 100, 'ro', markersize=8, label=r'$+1\text{ C}$')
plt.plot(x2 * 100, y2 * 100, 'bo', markersize=8, label=r'$-1\text{ C}$')
plt.title(r'Campo Elétrico Vetorial $\vec{E}$ (Grade de Flechas)')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("Figure_campo_flechas.png", dpi=150)

plt.show()

