# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:19:08 2025

@author: roger
"""

for i in range(1, 101):
    j = i + 1
    h = i + 2
    producto = i * j * h

    divisible = (producto % 6 == 0)

    if i % 2 == 0:
        multiplo_24 = (producto % 24 == 0)
    else:
        multiplo_24 = False 

    if divisible:
        print(f"{i:<5}{j:<5}{h:<5}{producto:<12}{str(divisible):<20}{str(multiplo_24):<30}")
        
        #%%
n = int(input("Ingrese un número entero mayor que 1: "))
num = n
factores = []
divisor = 2


while n > 1:
    if n % divisor == 0:
        factores.append(divisor)
        n //= divisor
    else:
        divisor += 1

print(f"\nNúmero: {num}")
print("Factor  Exponente")
print("------------------")

for p in sorted(set(factores)):
    print(f"{p:<8}{factores.count(p)}")
