# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 01:02:32 2019

@author: pablo gullith
"""
#Questão 4:
#Aluno: Pablo Gullith de Melo Dantas
def f(x):
    return x**4 - 2*x + 1
valorReal = 4.4

N = [10,100,1000]
a = 0.0
b = 2.0


def simp(a,b,N):
    area = f(a)
    h = (b-a)/N
    for i in range(1,N+1):
        if i == N:
            area += f(b)
        else:
            if i%2 != 0:
                area += 4*f(a+(i*h))
            else:
                area += 2*f(a+(i*h))
    return area*(h/3)
for i in range(len(N)):
    print("N:{} = {}".format(N[i],simp(a,b,N[i])))

print("Erro relativo: ", (simp(a,b,10)-valorReal)/valorReal)

#Alguns comentários:

#Valor obtido usando 10 fátias no método do trapézio:4.50656
#Valor obtido usando 10 fátias no método do simpson:4.400426666666667

#Os resultados obtidos atráves do método de simpson são melhores
#usando o método de simpson chega-se a resultados mais convictos
#exemplo disto é quando utilizamos apenas 10 fátias e o método de
#simpson nos retorna um resultado mais próximo do resultado real.
#a semelhança entre os dois métodos é que ambos melhoram seus resultados
#de acordo com o número de fátias adicionado.
