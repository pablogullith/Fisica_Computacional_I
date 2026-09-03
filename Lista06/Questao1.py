#Autor: Pablo Gullith
#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#Definir função
def f(x):
    return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
def f1(x):
    return 5544*x**5-13860*x**4+12600*x**3-5040*x**2+840*x-42

# Metodo de newton
Precisao=1e-10
def Raiz(f,f1,ValorInicial,Precisao):
    x=ValorInicial
    delta=f(x)/f1(x)
    while abs(delta)>Precisao:
        delta=f(x)/f1(x)
        x-=delta

    return x


print('Raiz1:',Raiz(f,f1,0,Precisao))
print('Raiz2:',Raiz(f,f1,0.2,Precisao))
print('Raiz3:',Raiz(f,f1,0.4,Precisao))
print('Raiz4:',Raiz(f,f1,0.6,Precisao))
print('Raiz5:',Raiz(f,f1,0.8,Precisao))
print('Raiz6:',Raiz(f,f1,0.95,Precisao))

#Gráfico
x=np.linspace(0,1,100)
Valores=list(map(f,x))
plt.plot(x,Valores,'r')
plt.savefig("Figure_1.png")
plt.show()
#As raízes por inspeção são, aproximadamente: 0.03, 0.17, 0.38, 0.62, 0.83, 0.96.

