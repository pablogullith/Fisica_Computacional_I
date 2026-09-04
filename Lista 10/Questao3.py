#Autor: Pablo Gullith
#Bibliotecas
from numpy import array, arange, pi, sin, cos, sqrt
from pylab import plot, show, xlabel, ylabel, title, savefig

#Constantes
g = 9.81
m = 1
R = 0.08
theta_0 = 30 * pi / 180  
v_0 = 100 
rho = 1.22
C = 0.47
t_0 = 0.0
t_f = 6.6
N = 10000
h = (t_f - t_0) / N


c = pi * R ** 2 * rho * C / 2
def Constantes_U(m):
    return c / m

def f(r, t, m):
    # x = r[0]
    vx = r[1]
    # y = r[2]
    vy = r[3]
    v = sqrt(vx ** 2 + vy ** 2)
    return array([vx, - Constantes_U(m) * vx * v,
                  vy, -g - Constantes_U(m) * vy * v], float)


pontos_t = arange(t_0, t_f, h)
def Trajetoria(m):
    pontos_x = []
    pontos_y = []
    r = array([0, v_0 * cos(theta_0), 0, v_0 * sin(theta_0)], float)
    for t in pontos_t:
        pontos_x.append(r[0])
        pontos_y.append(r[2])
        k1 = h * f(r, t, m)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, m)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, m)
        k4 = h * f(r + k3, t + h, m)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(pontos_x, float), array(pontos_y, float)

Trajetoria1_x, Trajetoria1_y = Trajetoria(1)
Trajetoria2_x, Trajetoria2_y = Trajetoria(2)
Trajetoria3_x, Trajetoria3_y = Trajetoria(4)
title('Trajetoria da bala de canhão')
plot(Trajetoria1_x, Trajetoria1_y, 'k')
xlabel('x (m)')
ylabel('y (m)')
savefig('trajetoria_bala.png')
show()
title('Trajetórias com pesos diferentes')
plot(Trajetoria1_x, Trajetoria1_y, 'k')
plot(Trajetoria2_x, Trajetoria2_y, 'g')
plot(Trajetoria3_x, Trajetoria3_y, 'b')
xlabel('x (m)')
ylabel('y (m)')
savefig('trajetorias_diferentes.png')
show()

#Alguns comentários:
""" Sabe-se que a massa é indiferente se o experimento for feito no vácuo, porém, se fizermos alguns experimentos como o da 
questão na vida real, temos que levar em consideração a resistência do ar que interfere na trajetória dos corpos de acordo
com sua massa."""