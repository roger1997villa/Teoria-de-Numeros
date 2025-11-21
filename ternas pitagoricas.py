# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:52:24 2025

@author: roger
"""
def mcd(a, b):
    """Calcula el máximo común divisor"""
    while b:
        a, b = b, a % b
    return a

def generar_ternas():
    ternas = []
    for a in range(2, 61):
        for b in range(1, a):
            if mcd(a, b) == 1:  # Primos relativos
                x = a*a - b*b
                y = 2*a*b
                z = a*a + b*b
                if 5 <= z <= 61 and x % 2 == 1:
                    ternas.append((x, y, z, a, b))
    return ternas

# Usar la función
ternas = generar_ternas()
print("Ternas pitagóricas (a y b primos relativos):")
for x, y, z, a, b in ternas:
    print(f"({x:2d}, {y:2d}, {z:2d}) - a={a}, b={b}")