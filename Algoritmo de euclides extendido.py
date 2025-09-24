# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 10:54:52 2025

@author: roger
"""

def Algoritmo_euclides(a,b):
    a
    b
    print(f"{'a':>5} {'b':>5} {'q':>3} {'r':>5} {'x':>6} {'y':>6}")
    print("--------------------------------------------------" )
    
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b != 0:
       q = a // b
       r = a % b
       x = x0 - q * x1
       y = y0 - q * y1
       print(f"{a:>5} {b:>5} {q:>3} {r:>5} {x:>6} {y:>6}")
       
       a, b = b, r
       x0, x1 = x1, x
       y0, y1 = y1, y

    print(f"\nel MCD es {a}")
    print(f"coeficientes x = {x0}, y = {y0}")
   
    
Algoritmo_euclides(1001, 275)
