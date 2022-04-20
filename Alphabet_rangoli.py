# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:08:12 2020

@author: Prital
"""
size = 3 #0 < n < 27
string = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, size + 1):
    res = ""
    
    for j in range(size - 1, size - i, -1):
        res = res + string[j] + "-"
    res = res + string[size - i]
    for j in range(size - i + 1, size):
        res = res + "-" + string[j]
    
    print(res.center(4 * size - 3, "-"))
    
for i in range(size - 1, 0, -1):
    res = ""
    
    for j in range(size - 1, size - i, -1):
        res = res + string[j] + "-"
    res = res + string[size - i]
    for j in range(size - i + 1, size):
        res = res + "-" + string[j]
    
    print(res.center(4 * size - 3, "-"))