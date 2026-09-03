#Autor: Pablo Gullith
#Bibliotecas
import numpy as np
from gaussxw import gaussxwab
import scipy.constants as sp
import matplotlib.pyplot as plt

#Dados da questão
h=6.62607004*1e-34
c=299792458
lambda1=390*1e-9
lambda2=750*1e-9
Boltzmann=1.38064852*1e-23
Inferior=h*c/(lambda2*Boltzmann)
Superior=h*c/(lambda1*Boltzmann)
z=(1+np.sqrt(5))/2 
Precisao=1 

#Definição
def eta(T):
    def f(x):
        return x**3/(np.exp(x)-1)
	#Quadratura gaussiana com N = 100 usando a gaussiana do mark newman.
    N=100
    x,w=gaussxwab(N,Inferior/T,Superior/T)
    integral=0.0
    for k in range(N):
        integral+=w[k]*f(x[k])

    return 15/np.pi**4*integral

#Grafíco
T=np.linspace(300,10000,100)
etas=list(map(eta,T))
plt.plot(T,etas,'k')
plt.xlabel('T(K)')
plt.ylabel("$\eta(T)$")
plt.savefig("Figure_2.png")
plt.show()

#Nesta parte, usaremos o método da seção áurea para calcular a eficiência máxima. Temos os pontos iniciais:
x1,x4=6000,8000
x2=(x1-x4)/sp.golden+x4
x3=sp.golden*(x2-x1)+x1
precisao=1
while abs(x4-x1)>precisao:
    if eta(x2)>eta(x3):
        x4=x3
        x3=x2
        x2=(x1-x4)/sp.golden+x4
    else:
        x1=x2
        x2=x3
        x3=sp.golden*(x2-x1)+x1

print("Temperatura de eficiência máxima:",((x1+x4)/2), "K")
#Alguns comentários:
"""É sabido que o ponto de fusão do tungstênio é algo próximo à 3695 Kelvin, Para esta temperatura é inviável usar
uma lâmpada de filamento de tungstênio"""