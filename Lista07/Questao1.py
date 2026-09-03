#Autor: Pablo Gullith	
#Bibliotecas
from __future__ import division, print_function
from numpy import array,empty
#Sistema
A = array([[ 4,-1,-1,-1 ],
           [ -1,3,0,-1 ],
           [ -1,0,3,-1 ],
           [ -1,-1,-1,4]], float)
v = array([ 5, 0, 5, 0 ],float)
N = len(v)

# Eliminação Gaussiana
for m in range(N):


    div = A[m,m]
    A[m,:] /= div
    v[m] /= div


    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]


x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print('SISTEMA SOLUCIONADO:\n',x)
#Linalg para ver se conseguimos de fato acertar a solução
from numpy.linalg import solve
A = array([[ 4,-1,-1,-1 ],
           [ -1,3,0,-1 ],
           [ -1,0,3,-1 ],
           [ -1,-1,-1,4]], float)
v = array([ 5, 0, 5, 0 ],float)
print('SISTEMA SOLUCIONADO VIA LINALG:\n',solve(A,v))