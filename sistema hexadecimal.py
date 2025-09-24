

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 10:40:00 2025

@author: AULA
"""

def hexagesimal():
    vector = []
    vector1 = ("A", "B", "C", "D", "E","F")
    n = int(input("ingrese el numero el cual desea ver en el sistema hexagesimal: "))
    if n == 0:
        print ("0")
        
    if n < 0:
         n = abs(n)
    
    while n >= 16:
        r = n%16
        n = n//16
        if r == 10:
            vector.append(vector1[0])
        elif r  == 11:
           vector.append(vector1[1])
        elif r  == 12:
            vector.append(vector1[2])
        elif r  == 13:
            vector.append(vector1[3])
        elif r == 14:
            vector.append(vector1[4])
        elif r == 15:
            vector.append(vector1[5])
        elif 0<=r <10:
            vector.append(r)
    if n == 10:
        vector.append(vector1[0])
    elif n  == 11:
       vector.append(vector1[1])
    elif n  == 12:
        vector.append(vector1[2])
    elif n == 13:
        vector.append(vector1[3])
    elif n == 14:
        vector.append(vector1[4])
    elif n == 15:
        vector.append(vector1[5])  
  
    if 0<=n<10:
        vector.append(n)
   
    
            
    vector.reverse()
    print(vector)
        
    
    
    #%%
tabla= hexagesimal()