#Autor: Pablo Gullith
#Bibliotecas
from numpy import array, arange
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
sigma = 10
r = 28
b = 8 / 3
t_0 = 0
t_f = 50
x_0 = 0
y_0 = 1
z_0 = 0
N = 100000
h = (t_f - t_0) / N

def f_x(x, y, z):
    return sigma * (y - x)


def f_y(x, y, z):
    return r * x - y - x * z


def f_z(x, y, z):
    return x * y- b * z


def f(r):
    x = r[0]
    y = r[1]
    z = r[2]
    return array([f_x(x, y, z), f_y(x, y, z), f_z(x, y, z)], float)

pontos_t = arange(t_0, t_f, h)
pontos_x = []
pontos_y = []
pontos_z = []
R = array([x_0, y_0, z_0], float)
for t in pontos_t:
    pontos_x.append(R[0])
    pontos_y.append(R[1])
    pontos_z.append(R[2])
    k1 = h * f(R)
    k2 = h * f(R + 0.5 * k1)
    k3 = h * f(R + 0.5 * k2)
    k4 = h * f(R+k3)
    R += (k1 + 2 * k2 + 2 * k3 + k4)/6

#Gráfico estranho atrator
plot(pontos_x,pontos_z,'k')
xlabel('t')
ylabel('y(t)')
savefig("lorenz_attractor.png")
show()
#Grafico função em relação a tempo
#plot(pontos_t,pontos_x)
plot(pontos_t,pontos_y)
xlabel("t")
savefig("lorenz_phase_space.png")
show()
