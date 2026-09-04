#Autor: Pablo Gullith
#Bibliotecas:
import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M_SOL = 1.9891e30
SEGUNDOS_POR_ANO = 365.25 * 24 * 3600
MU = G * M_SOL * SEGUNDOS_POR_ANO**2

X0 = 4.0e12
Y0 = 0.0
VX0 = 0.0
VY0 = 500.0 * SEGUNDOS_POR_ANO

DELTA_POSICAO = 1.0e3


def derivada(estado):
    """Retorna (vx, ax, vy, ay) para o estado (x, vx, y, vy)."""
    x, vx, y, vy = estado
    raio = np.hypot(x, y)
    aceleracao = -MU / raio**3
    return np.array([vx, aceleracao * x, vy, aceleracao * y], dtype=float)


def rk4_passo(estado, passo):
    """Executa um passo do metodo de Runge-Kutta de quarta ordem."""
    k1 = passo * derivada(estado)
    k2 = passo * derivada(estado + 0.5 * k1)
    k3 = passo * derivada(estado + 0.5 * k2)
    k4 = passo * derivada(estado + k3)
    return estado + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def periodo_orbital(estado_inicial):
    """Calcula o periodo pela energia orbital especifica."""
    x, vx, y, vy = estado_inicial
    raio = np.hypot(x, y)
    velocidade_quadrada = vx**2 + vy**2
    energia_especifica = 0.5 * velocidade_quadrada - MU / raio
    semieixo_maior = -MU / (2 * energia_especifica)
    return 2 * np.pi * np.sqrt(semieixo_maior**3 / MU)


def orbita_passo_fixo(estado_inicial, tempo_final, passo):
    tempos = [0.0]
    estados = [estado_inicial.copy()]
    estado = estado_inicial.copy()
    tempo = 0.0

    while tempo < tempo_final:
        passo_atual = min(passo, tempo_final - tempo)
        estado = rk4_passo(estado, passo_atual)
        tempo += passo_atual
        tempos.append(tempo)
        estados.append(estado.copy())

    return np.array(tempos), np.array(estados)


def orbita_passo_adaptativo(estado_inicial, tempo_final, passo_inicial):
    tempos = [0.0]
    estados = [estado_inicial.copy()]
    estado = estado_inicial.copy()
    tempo = 0.0
    passo = passo_inicial
    passo_minimo = 1.0e-8

    while tempo < tempo_final:
        passo = min(passo, tempo_final - tempo)
        passo_teste = rk4_passo(estado, passo)
        estado_meio = rk4_passo(estado, passo / 2)
        estado_dois_meios = rk4_passo(estado_meio, passo / 2)

        erro_posicao = np.linalg.norm(estado_dois_meios[[0, 2]] - passo_teste[[0, 2]]) / 15
        tolerancia = DELTA_POSICAO * passo

        if erro_posicao <= tolerancia or passo <= passo_minimo:
            tempo += passo
            estado = estado_dois_meios
            tempos.append(tempo)
            estados.append(estado.copy())

        if erro_posicao == 0:
            fator = 2.0
        else:
            fator = 0.9 * (tolerancia / erro_posicao) ** 0.2
        passo = np.clip(passo * fator, 0.1 * passo, 2.0 * passo)

    return np.array(tempos), np.array(estados)


estado_inicial = np.array([X0, VX0, Y0, VY0], dtype=float)
periodo = periodo_orbital(estado_inicial)
tempo_final = 2.0 * periodo
passo_fixo = periodo / 20000

# Partes (a) e (b): duas orbitas com passo fixo.
tempo_fixo, estados_fixos = orbita_passo_fixo(estado_inicial, tempo_final, passo_fixo)

# Parte (c): duas orbitas com passo adaptativo.
tempo_adaptativo, estados_adaptativos = orbita_passo_adaptativo(
    estado_inicial, tempo_final, periodo / 100
)

print(f"Periodo orbital: {periodo:.6f} anos")
print(f"Passo fixo: {passo_fixo:.6e} anos")
print(f"Passos fixos: {len(tempo_fixo) - 1}")
print(f"Passos adaptativos: {len(tempo_adaptativo) - 1}")
print(f"Passo adaptativo minimo: {np.min(np.diff(tempo_adaptativo)):.6e} anos")
print(f"Passo adaptativo maximo: {np.max(np.diff(tempo_adaptativo)):.6e} anos")

# Parte (c): orbitas sucessivas devem coincidir.
fig_fixo, eixo_fixo = plt.subplots(figsize=(7, 6))
eixo_fixo.plot(estados_fixos[:, 0] / 1e12, estados_fixos[:, 2] / 1e12)
eixo_fixo.set_title("RK4 com passo fixo")
eixo_fixo.set_xlabel("x (10^12 m)")
eixo_fixo.set_ylabel("y (10^12 m)")
eixo_fixo.set_aspect("equal")
fig_fixo.tight_layout()
fig_fixo.savefig("orbita_cometa_passo_fixo.png", dpi=150)

# Parte (d): resultado do passo adaptativo.
fig_adaptativo, eixo_adaptativo = plt.subplots(figsize=(7, 6))
eixo_adaptativo.plot(
    estados_adaptativos[:, 0] / 1e12,
    estados_adaptativos[:, 2] / 1e12,
)
eixo_adaptativo.set_title("RK4 com passo adaptativo")
eixo_adaptativo.set_xlabel("x (10^12 m)")
eixo_adaptativo.set_ylabel("y (10^12 m)")
eixo_adaptativo.set_aspect("equal")
fig_adaptativo.tight_layout()
fig_adaptativo.savefig("orbita_cometa_passo_adaptativo.png", dpi=150)

# Parte (e): pontos de cada passo durante uma orbita.
orbita_um_ano = tempo_adaptativo <= periodo
passos_orbita = estados_adaptativos[orbita_um_ano]
fig_passos, eixo_passos = plt.subplots(figsize=(7, 6))
eixo_passos.plot(
    passos_orbita[:, 0] / 1e12,
    passos_orbita[:, 2] / 1e12,
    "o-",
    markersize=2,
)
eixo_passos.set_title("Passos durante uma orbita")
eixo_passos.set_xlabel("x (10^12 m)")
eixo_passos.set_ylabel("y (10^12 m)")
eixo_passos.set_aspect("equal")
fig_passos.tight_layout()
fig_passos.savefig("passos_cometa.png", dpi=150)

plt.show()
