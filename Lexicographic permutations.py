# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:42:30 2021

@author: Prital Bamnodkar
"""

# A permutation is an ordered arrangement of objects. For example,
#     3124 is one possible permutation of the digits 1, 2, 3 and 4. 
#     If all of the permutations are listed numerically or alphabetically, 
#     we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def Permutations(string):
    
    if len(string) <= 1:
        return string
    else:
        out = []
        
        for char in string:
            rest_of_char = string.replace(char, '', 1)
            perm_rest_of_char = Permutations(rest_of_char)
            
            for perm in perm_rest_of_char:
                out.append(char + perm)
                
        return out

print(Permutations('0123456789')[999999])