#Autor: Pablo Gullith
#Bibliotecas
from numpy import sqrt, zeros, copy, array
from numpy.linalg import solve
A = array([[2,1,4,1],
		  [3,4,-1,-1],
		  [1,-4,1,5],
		  [2,-2,1,3]],float)

v = array([-4,3,9,7],float)		  
#Solução via linalg
linal = solve(A,v)
print('RESOLUCAO DO SISTEMA VIA LINALG:')
print(linal)

def Decomposicao_Lu(A):
    
    N = int(sqrt(A.size))
    L = zeros((N,N))
    U = copy(A)
    
    for i in range(N):
        
        for n in range(i,N):
            
            L[n,i] = U[n,i]
        p = U[i,i]
        for j in range(i,N):
            U[i,j]=U[i,j]/p
            
        for k in range(i+1,N):
            q= -U[k,i]
            for l in range(i,N):
                U[k,l]=U[k,l]+q*U[i,l]
    return L,U
#Definição
def Primeira(L,v):
    N = v.size
    y = zeros(N,float)

    for i in range(N):
        y[i] = v[i]
        
        for j in range(i):
            y[i] = y[i] - L[i,j]*y[j]
            
        y[i] = y[i]/L[i,i]
    return y
#Definição
def Segunda(U,y):
    
    N = y.size
    x = zeros(N,float)
    
    for i in range(N-1,-1,-1):
        x[i] = y[i]
        for j in range(i+1,N):
            x[i] = x[i] - U[i,j]*x[j]
    return x

L,U = Decomposicao_Lu(A)
y = Primeira(L,v)
x = Segunda(U,y)

print('RESOLUÇÃO DO SISTEMA DENOMINADO COMO (PRIMEIRA):')
print(y)
print('RESOLUÇÃO DO SISTEMA DEMONINADO COMO (SEGUNDA):')
print(x)            
    
