#Autor: Pablo Gullith
#Bibliotecas
from numpy import array, arange
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
omega = 1
t_0 = 0
t_f = 50
x_0 = 1
v_0 = 0
N = 5000
h = (t_f - t_0) / N

def f_harmonico(r, t):
    x = r[0]
    v = r[1]
    return array([v, - omega ** 2 * x], float)

pontos_t = arange(t_0, t_f, h)
def x_harmonico(amplitude):
    pontos_x = []
    r = [amplitude, v_0]
    for t in pontos_t:
        pontos_x.append(r[0])
        k1 = h * f_harmonico(r, t)
        k2 = h * f_harmonico(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f_harmonico(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f_harmonico(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(pontos_x, float)

def f_anarmonico(r, t):
    x = r[0]
    v = r[1]
    return array([v, - omega ** 2 * x ** 3], float)

def x_anarmonico(amplitude):
    pontos_x = []
    pontos_v = []
    r = array([amplitude, v_0], float)
    for t in pontos_t:
        pontos_x.append(r[0])
        pontos_v.append(r[1])
        k1 = h * f_anarmonico(r, t)
        k2 = h * f_anarmonico(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f_anarmonico(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f_anarmonico(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(pontos_x, float), array(pontos_v, float)


plot(pontos_t, x_anarmonico(x_0)[0])
plot(pontos_t, x_anarmonico(2 * x_0)[0])
xlabel('t (s)')
ylabel('x (m)')
savefig("anarmonico.png")
show()

x, v = x_anarmonico(x_0)
plot(x, v)
xlabel('x')
ylabel('v')
savefig("anarmonico_fase.png")
show()


#Constantes
t_f = 20
N = 10000
h = (t_f - t_0) / N
def g(r, t, mu):
    x = r[0]
    v = r[1]
    return array([v, mu * (1 - x ** 2) * v - omega ** 2 * x], float)

pontos_t = arange(t_0, t_f, h)

def x_van_der_pol(mu):
    pontos_x = []
    pontos_v = []
    r = array([x_0, v_0], float)
    for t in pontos_t:
        pontos_x.append(r[0])
        pontos_v.append(r[1])
        k1 = h * g(r, t, mu)
        k2 = h * g(r + 0.5 * k1, t + 0.5 * h, mu)
        k3 = h * g(r + 0.5 * k2, t + 0.5 * h, mu)
        k4 = h * g(r + k3, t + h, mu)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(pontos_x, float), array(pontos_v, float)


mu1_x, mu1_v = x_van_der_pol(1)
mu2_x, mu2_v = x_van_der_pol(2)
mu3_x, mu3_v = x_van_der_pol(4)
plot(mu1_x, mu1_v, 'r')
plot(mu2_x, mu2_v, 'b')
plot(mu3_x, mu3_v, 'g')
xlabel('x')
ylabel('v')
savefig("van_der_pol_fase.png")
show()