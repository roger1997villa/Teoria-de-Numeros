00# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 10:52:54 2025

@author: AULA
"""

n1 = int(input("ingrese el primer numero que desea hallar el mcm: "))
n2 = int(input("ingrese el segundo numero que desea hallar el mcm: "))


m1 = []
m2 = []

a = n1 * n2

for i in range(1,a+1):
    m1.append(n1 * i)
    m2.append(n2 * i)
    
mcm = None
for j in m1 : 
    if j in m2:
        mcm = j
        break
    
print(f"el mcm de {n1} y {n2} es {mcm}")

#%%

n1 = int(input("ingrese el primer numero que desea hallar el mcd: "))
n2 = int(input("ingrese el segundo numero que desea hallar el mcd: "))


m1 = []
m2 = []



for i in range(1, n1+1):
    if n1 % i == 0:
        m1.append (i)
for i in range(1, n2+1):
    if n2 % i == 0:
        m2.append (i)
    
mcd = None
for j in m1 : 
    if j in m2:
        mcd = j
        
    
print(f"el mcd de {n1} y {n2} es {mcd}")