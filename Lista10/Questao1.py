#Autor: Pablo gullith
#Bibliotecas
from numpy import sin, cos, array, arange, sqrt
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
C = 2
l = 0.1
theta_0 = 0.0
omega_0 = 0.0
t_0 = 0.0
t_max = 100
g = 9.81
N = 5000
h = (t_max - t_0) / N

def f(r, t, Omega):
    theta = r[0]
    omega = r[1]
    return array([omega, -(g / l) * sin(theta) + C * cos(theta) * sin(Omega * t)], float)


def theta(Omega):
    pontos_t = arange(t_0, t_max, h)
    pontos_theta = []
    r = array([theta_0, omega_0], float)
    for t in pontos_t:
        pontos_theta.append(r[0])
        k1 = h * f(r, t, Omega)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, Omega)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, Omega)
        k4 = h * f(r + k3, t + h, Omega)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return pontos_theta


pontos_t = arange(t_0, t_max, h)
xlabel("Tempo (s)")
ylabel("Angulo (rad)")
plot(pontos_t, theta(5), 'c')
savefig("pendulo_forcado.png")
show()
plot(pontos_t, theta(sqrt(g/l)), 'c')
xlabel("Tempo (s)")
ylabel("Angulo (rad)")
savefig("pendulo_forcado_ressonancia.png")
show()