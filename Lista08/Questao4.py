#Autor: Pablo gullith
#Bibliotecas
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt

def f(m, n):
    if m == n:
        return L/2
    else:
        return 0

def g(m, n): 
    if m == n:
        return (L**2)/4
    elif m%2 == n%2:
        return 0
    else:
        return -((2*L/np.pi)**2)*m*n/((m**2 - n**2)**2)

def H(m, n):
    A = (h**2)*(np.pi**2)*(n**2)/M/(L**3)
    B = 2*a/(L**2)
    
    return A*f(m, n) + B*g(m, n)

def matriz_H(N):
    A = np.empty([N, N], float)
    for m in range(N):
        for n in range(N):
            A[m, n] = H(m + 1, n + 1)
    return A

L = 5e-10 
h = 197.32697e-9 
a = 10 
M = 0.511e6 

H10 = matriz_H(10)
H100 = matriz_H(100)

print("Matriz 10X10:\n\n", npl.eigvalsh(H10), "\nMatriz 100X100:\n\n", npl.eigvalsh(H100)[:10])

# Item (e): densidades de probabilidade dos tres primeiros estados.
energias, coeficientes = npl.eigh(H100)
x = np.linspace(0, L, 1000)
indices = np.arange(1, 101)[:, np.newaxis]
base_seno = np.sin(np.pi * indices * x / L)
funcoes_onda = np.sqrt(2 / L) * (coeficientes[:, :3].T @ base_seno)

plt.figure()
for estado in range(3):
    densidade = np.abs(funcoes_onda[estado]) ** 2
    normalizacao = np.trapezoid(densidade, x)
    print(f"Normalizacao do estado {estado}: {normalizacao:.8f}")
    plt.plot(x * 1e10, densidade, label=f"Estado {estado}")

plt.xlabel("x (Angstrom)")
plt.ylabel("|psi(x)|^2 (1/m)")
plt.title("Densidade de probabilidade no poco quantico")
plt.legend()
plt.tight_layout()
plt.savefig("densidade_probabilidade.png", dpi=300)
plt.show()

""" Alguns comentários: 
Quando fazemos novamente o calculo para 100x100 é pequeno o ganho de precisão em temperaturas baixas. É perceptivel
que quando os números quanticos crescem é viável aumentar a quantidade de termos do hamiltoniano para podermos calcular
os autovalores.""" 


