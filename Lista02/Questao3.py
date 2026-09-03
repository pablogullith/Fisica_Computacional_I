# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:09:42 2019

@author: pablo gullith
"""
#Questão 3:
#Aluno: Pablo Gullith de Melo Dantas
from __future__ import division, print_function

def f(x):
    return x**4 - 2*x + 1


# Regra do trapézio para integração numérica
def integrate(f, a, b, N=20):
    h = (b - a) / N
    s = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, N):
        s += f(a + k * h)
    return h * s

# Avaliação da integral com N1 = 10 e N2 = 20 fatias
I1 = integrate(f, 0, 2, 10)
I2 = integrate(f, 0, 2, 20)

# Estimativa prática do erro pela fórmula: epsilon2 = (1/3) * (I2 - I1)
epsilon2 = (1.0 / 3.0) * (I2 - I1)

# Erro real através da comparação com o valor analítico 4.4
valor_exato = 4.4
diferenca = valor_exato - I2

print("=== Questão 3: Regra do Trapézio e Estimativa do Erro ===")
print("Integral com N = 10 fatias (I1): {:12.8f}".format(I1))
print("Integral com N = 20 fatias (I2): {:12.8f}".format(I2))
print("Valor analítico exato:           {:12.8f}".format(valor_exato))
print("-" * 55)
print("Erro prático estimado (epsilon2): {:12.8f}".format(epsilon2))
print("Erro real (4.4 - I2):             {:12.8f}".format(diferenca))
print("Diferença entre os dois erros:    {:12.8f}".format(abs(epsilon2 - diferenca)))
print()

# Respostas conceituais pedidas no enunciado:
print("--- Respostas conceituais ---")
print("1. Como o erro estimado se compara com a diferenca real?")
print("   Ambos sao extremamente proximos: epsilon2 ~ {:.6f} e (4.4 - I2) ~ {:.6f},".format(epsilon2, diferenca))
print("   concordando ate a quarta casa decimal (diferenca de apenas ~2.7e-5).")
print()
print("2. Por que os dois não concordam perfeitamente?")
print("   A fórmula prática epsilon2 = (1/3)*(I2 - I1) é deduzida a partir da expansão")
print("   do erro da regra do trapézio (série de Euler-Maclaurin), considerando apenas")
print("   o termo dominante de ordem O(h^2) e desprezando ordens superiores.")
print("   Como f(x) = x^4 - 2x + 1 possui derivadas de ordem superior não nulas, há termos")
print("   residuais de ordem O(h^4) e maiores que causam essa pequena discrepância.")
