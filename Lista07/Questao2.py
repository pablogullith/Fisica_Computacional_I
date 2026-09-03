#Autor: Pablo Gullith
#Bibliotecas
from numpy import array, empty, copy
#Eliminação Gaussiana def
def Eliminacao_Gaussiana(A, v):

    N = len(v)
    #Eliminação Gaussiana
    for m in range(N):
        #Pivotização
        largest = abs(A[m, m])
        largest_row = m
        for i in range(m + 1, N):
            if abs(A[i, m]) > largest:
                largest = abs(A[i, m])
                largest_row = i
        if largest_row != m:
            
            current_row = copy(A[m, :])  
            A[m, :] = A[largest_row, :]
            A[largest_row, :] = current_row

            
            v[m], v[largest_row] = v[largest_row], v[m]

        
        div = A[m,m]
        A[m, :] /= div
        v[m] /= div

        
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    
    x = empty(N, float)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i] * x[i]

    return x
#Primeiro sistema
A = array([[2, 0, 4, 0],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
print('SOLUÇÃO DO PRIMEIRO SISTEMA:\n',Eliminacao_Gaussiana(A, v))
#Segundo sistema
B = array([[0, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)
w = array([ -4, 3, 9, 7 ], float)
print('SOLUÇÃO DO SEGUNDO SISTEMA:\n',Eliminacao_Gaussiana(B, w))