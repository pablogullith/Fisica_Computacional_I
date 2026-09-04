#Autor: Pablo Gullith
#Bibliotecas
import numpy as np
import banded as bd

def matriz(N):
    A = np.zeros([5, N], float)
    for j in range(N - 2):
        A[0, j + 2] = A[4, j] = -1
    for j in range(N - 1):
        A[1, j + 1] = A[3, j] = -1
    for j in range(N - 2):
        A[2, j + 1] = 4
    A[2, 0] = A[2, N - 1] = 3
    
    v = np.zeros(N, float)
    v[0] = v[1] = 5
    
    return A, v

A, v = matriz(6)
print("QUANDO N = 6:\n", bd.banded(A, v, 2, 2))

A, v = matriz(10000)
print("QUANDO N = 10000:\n", bd.banded(A, v, 2, 2))
        