#Autor:Pablo Gullith
#Bibliotecas:
from numpy import array, arange
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
h = 0.001
x_0 = 1
x_p_0 = 0
t_0 = 0
t_f = 50

def f(r):
    x = r[0]
    v = r[1]
    return array([ v, v ** 2 - x -5 ], float)

r = array([x_0, x_p_0] , float)
pontos_t = arange(t_0, t_f, h)
pontos_x = []
for t in pontos_t:
    pontos_x.append(r[0])
    r_mid = r + 0.5 * h * f(r)
    r += h * f(r_mid)


plot(pontos_t, pontos_x)
xlabel('t')
ylabel('x(t)')
savefig('solucao_ode.png')
show()