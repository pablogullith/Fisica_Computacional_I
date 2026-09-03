#Autor: Pablo Gullith
#Bibliotecas 
import numpy as np
#Dados da questão
m=7.348*1e22
R=3.844*1e8
omega=2.662*1e-6
Precisao=1e-8
G=6.674*1e-11
M=5.974*1e24
#Definição da Função
def f(r):
    return G*M*(R-r)**2-G*m*r**2-omega**2*r**3*(R-r)**2

def f1(r):
    return -2*G*M*(R-r)-2*G*m*r-3*omega**2*r**2*(R-r)**2\
           +2*omega**2*r**3*(R-r)
#Aplicar o metodo de newtom para achar as raizes
def Raiz(f,g,ValorInicial,Precisao):
    x=ValorInicial
    delta=f(x)/g(x)
    while abs(delta)>Precisao:
        delta=f(x)/g(x)
        x-=delta

    return x

r=Raiz(f,f1,3.2*1e8,Precisao)
print('VALOR DE r NO PONTO L1:',r,'M')