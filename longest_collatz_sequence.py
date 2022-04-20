# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:54:45 2021

@author: Prital Bamnodkar
"""

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence(n):
    res = [n]
    
    if n == 0:
        return None
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        res.append(n)
        
    return res

def collatz_multiple(n):
    # return a list of collatz sequences for all numbers less than n
    collatz_list = []
    
    for i in range(1, n):
        collatz_list.append(collatz_sequence(i))
        
    return collatz_list

def print_list(ls):
    for item in ls:
        print('-' * 5, '\n', item, '\n')
        
def biggest_list(ls):
    res = []
    
    for item in ls:
        if len(item) > len(res):
            res = item
            
    return res

n = 1000000

collatz = collatz_multiple(n)
biggest = biggest_list(collatz)

print(biggest)

