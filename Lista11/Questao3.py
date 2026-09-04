#Autor: Pablo Gullith
#Bibliotecas:
from numpy import array, arange, sqrt
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
x_0 = 1.4710 * 10 ** 11
vx_0 = 0
y_0 = 0
vy_0 = 3.0287 * 10 ** 4 * 8760 * 60 * 60  
t_0 = 0
t_f = 4 
h = 1 / 8760  # Uma hora em anos 
G = 6.6738 * 10 ** -11 * ( 8760 * 60 * 60) ** 2
M = 1.9891 * 10 ** 30  # Massa do sol em quilogramas
m = 5.9722 * 10 ** 24  # Massa da terra em quilogramas


def f(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    dist = sqrt(x ** 2 + y ** 2)
    return array([ vx, -G * M * x / dist ** 3, vy, -G * M * y / dist ** 3 ], float)


#Para calcular a orbita
pontos_t = arange(t_0, t_f, h)
pontos_x = []
pontos_y = []
Energia_potencial = []
Energia_cinetica = []
r = array([x_0, vx_0, y_0, vy_0], float)
f_mid = 0.5 * h * f(r)
vx_mid = r[1] + f_mid[1]
vy_mid = r[3] + f_mid[3]
for t in pontos_t:
    pontos_x.append(r[0])
    pontos_y.append(r[2])
    Energia_potencial.append(-6.6738 * 10 ** -11 * M * m / sqrt(r[0] ** 2 + r[2] ** 2))
    Energia_cinetica.append(0.5 * m * (r[1] ** 2 + r[3] ** 2) / (8760 * 60 * 60) ** 2)
    r[0] += h * vx_mid
    r[2] += h * vy_mid
    k = h * f(r)
    r[1] = vx_mid + 0.5 * k[1]
    r[3] = vy_mid + 0.5 * k[3]
    f_mid = 0.5 * h * f(r)
    vx_mid += k[1]
    vy_mid += k[3]


#Plotando orbita
plot(pontos_x, pontos_y)
xlabel('x (m)')
ylabel('y (m)')
savefig('orbita_terra.png')
show()


#Plotando as energias
Energia_total = array(Energia_cinetica, float) + array(Energia_potencial, float)
plot(pontos_t, Energia_cinetica, 'r')
plot(pontos_t, Energia_potencial, 'b')
plot(pontos_t, Energia_total, 'k')
xlabel('t (anos)')
ylabel('Energias (J)')
savefig('energias_terra.png')
show()
plot(Energia_total,'c')
savefig('energia_total_terra.png')
show()