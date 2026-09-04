#Autor: Pablo gullith
#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#Constantes
g = 9.81
l = 0.1
theta_0 = 179 * np.pi / 180
omega_0 = 0.0
t_0 = 0.0
t_max = 10.0
N = 5000
h = (t_max - t_0) / N

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g / l) * np.sin(theta)
    return np.array([ftheta, fomega], float)


#Runge Kutta de quarta ordem
pontos_t = np.arange(t_0, t_max, h)
pontos_theta = []
r = np.array([theta_0, omega_0], float)
for t in pontos_t:
    pontos_theta.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Gráfico do angulo em funcao do tempo.
fig_grafico, ax_grafico = plt.subplots()
ax_grafico.plot(pontos_t, np.array(pontos_theta) * 180 / np.pi)
ax_grafico.set_xlabel("Tempo (s)")
ax_grafico.set_ylabel("Angulo (graus)")
ax_grafico.set_title("Pendulo simples")
plt.savefig("pendulo_simples.png")
plt.show()

# # Animacao do pendulo usando Matplotlib.
# fig_animacao, ax_animacao = plt.subplots()
# ax_animacao.set_aspect("equal")
# ax_animacao.set_xlim(-1.15 * l, 1.15 * l)
# ax_animacao.set_ylim(-1.15 * l, 0.15 * l)
# ax_animacao.set_xlabel("x (m)")
# ax_animacao.set_ylabel("y (m)")
# ax_animacao.set_title("Movimento do pendulo")
# ax_animacao.grid(True)

# haste, = ax_animacao.plot([], [], "-", color="black", linewidth=2)
# massa, = ax_animacao.plot([], [], "o", color="tab:blue", markersize=12)

# def inicializar():
#     haste.set_data([], [])
#     massa.set_data([], [])
#     return haste, massa

# def atualizar(indice):
#     theta = pontos_theta[indice]
#     x = l * np.sin(theta)
#     y = -l * np.cos(theta)
#     haste.set_data([0, x], [0, y])
#     massa.set_data([x], [y])
#     return haste, massa

# animacao = FuncAnimation(
#     fig_animacao,
#     atualizar,
#     frames=len(pontos_theta),
#     init_func=inicializar,
#     interval=1000 * h,
#     blit=True,
# )

# plt.show()