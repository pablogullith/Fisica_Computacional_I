#Autor: Pablo Gullith
#Bibliotecas 
from numpy import floor, arange
from pylab import plot, show, xlabel, ylabel, savefig

#Constantes
V_saida_0 = 0
t_inicial = 0
t_final = 10
N = 5000 
h = (t_final - t_inicial) / N

#Definições
def V_entrada(t):
    if floor(2 * t) % 2 == 0:
        return 1
    else:
        return -1


def f(V, t, RC):
    return 1 / RC * (V_entrada(t) - V)


def g(RC):
    pontos_t = arange(t_inicial, t_final, h)
    pontos_v = []
    V = V_saida_0
    for t in pontos_t:
        pontos_v.append(V)
        k1 = h * f(V, t, RC)
        k2 = h * f(V + 0.5 * k1, t + 0.5 * h, RC)
        k3 = h * f(V + 0.5 * k2, t + 0.5 * h, RC)
        k4 = h * f(V + k3, t + h, RC)
        V +=  (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return pontos_v

#Plots
t = arange(t_inicial, t_final, h)
plot(t, g(0.01),'k')
savefig("V_saida_RC_0.01.png")
show()
xlabel('t')
ylabel('V(t)')
plot(t, g(0.1),'k')
savefig("V_saida_RC_0.1.png")
show()
xlabel('t')
ylabel('V(t)')
plot(t, g(1),'k')
savefig("V_saida_RC_1.png")
show()
xlabel('t')
ylabel('V(t)')

#alguns comentários
"""Quando o produto RC aumenta, temos a amplitude de voltagem da saída diminuindo. O circuito filtra as frequências altas,
quando comparamos à frequência caracteristica 1/(RC). Também é perceptível que o sinal de saida nos mostra uma onda triangular
Com isso tiramos que Vsaída é proporcional a integral de vin. Lembramos que tal comportamento é demoninado por circuito integrador"""