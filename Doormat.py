# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:24:39 2020

@author: Prital Bamnodkar
"""
n = 11 #odd natural number
m = 3 * n

x = int((m - 3) / 2) #width of smaller triangles

for i in range(n // 2):
    print((".|." * i).rjust(x, "-") + ".|." + ('.|.' * i).ljust(x, "-"))
    
print("WELCOME".center(m, "-"))

for i in range(n // 2 - 1, -1, -1):
    print((".|." * i).rjust(x, "-") + ".|." + ('.|.' * i).ljust(x, "-"))