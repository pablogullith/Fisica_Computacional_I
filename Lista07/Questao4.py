#Autor: Pablo Gullith
#Bibliotecas
from numpy.linalg import solve
from numpy import array

R1=R3=R5=1000
R2=R4=R6=2000 
C1=1e-6 
C2=0.5*1e-6 
xp=3
omega=1000

A=array([[1/R1+1/R4+1j*omega*C1,-1j*omega*C1,0],
            [-1j*omega*C1,1/R2+1/R5+1j*omega*C1+1j*omega*C2,-1j*omega*C2],
            [0,-1j*omega*C2,1/R3+1/R6+1j*omega*C2]],complex)
v=array([xp/R1,xp/R2,xp/R3],complex)

x=solve(A,v)
print('SOLUÇÃO PARA AS EQUAÇÕES:\n')

for i in range(len(x)):

	print(x[i],end=' ')