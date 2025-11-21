# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 06:06:30 2025

@author: roger
"""
# Lista de posibles valores de p
p_valores = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("Números perfectos generados con la fórmula n = 2^(p-1) * (2^p - 1):\n")

for p in p_valores:
    n = (2 ** (p - 1)) * ((2 ** p) - 1)
    print(f"p = {p}, n = {n}")


#%%
# Lista de posibles valores de p
p_valores = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("Números de mersenne generados con la fórmula n = 2^(p-1) ")

for p in p_valores:
    n = (2 ** (p )-1)
    print(f"p = {p}, n = {n}")
 #%%
 
 # Imprime los primeros números de Fermat
for n in range(1, 11):  # Cuidado: crecen muy rápido
    fermat = 2 ** (2 ** n) + 1
    print(f"F_{n} = {fermat:,}")  # Usa coma como separador de miles

#%%
def P(a, p):
    """Calcula P(a) = p**a - p**(a-1)."""
    return p**a - p**(a-1)

p_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for a in range(1,6):
    for p in p_list:
        print(f"P({a}, {p}) = {P(a, p)}")


#%%


