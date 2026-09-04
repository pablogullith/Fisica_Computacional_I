#Autor: Pablo Gullith
#Bibliotecas
from numpy import array, arange
from matplotlib.pyplot import plot, show, xlabel, ylabel, savefig

#Constantes
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2
x_0 = 2
y_0 = 2
t_inicial = 0
t_maximo = 30
N = 20000
h = (t_maximo - t_inicial) / N

def f_x(x, y):
    return alpha * x - beta * x * y


def f_y(x, y):
    return gamma * x * y - delta * y


def f(r):
    x = r[0]
    y = r[1]
    return array([ f_x(x, y), f_y(x, y) ] , float)


pontos_t = arange(t_inicial, t_maximo, h)
pontos_x = []
pontos_y = []

r = array([ x_0, y_0 ], float)
for t in pontos_t:
    pontos_x.append(r[0])
    pontos_y.append(r[1])
    k1 = h * f(r)
    k2 = h * f(r + 0.5 * k1)
    k3 = h * f(r + 0.5 * k2)
    k4 = h * f(r + k3)
    r += (k1 + 2 * k2 + 2 * k3 + k4)/6

plot(pontos_t, pontos_x, 'c')
plot(pontos_t, pontos_y, 'k')
xlabel('t')
ylabel('x(t), y(t)')
savefig("coelhos_raposas.png")
show()
#alguns comentários
"""Quando a curva dos coelhos chega ao máximo, a curva das raposas começa a crescer, sai da origem e começa seu crescimento. 
Isso nos faz pensar que quando o número de raposas é menor, o número de coelhos aumenta. Olhando o gráfico vemos que quando
a curva das raposas chega no máximo, a curva dos coelhos cai; isso nos mostra que muitos coelhos estão sendo caçados. 
Percebe-se também que quando a curva de coelhos cai, a curva de raposas também cai; isso demonstra a falta de coelhos para
caçar. No final do gráfico é mostrado uma queda de raposas e um aumento no número de coelhos."""





