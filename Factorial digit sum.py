# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:46:59 2021

@author: Prital Bamnodkar
"""

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n):
    out = 1
    
    for i in range(n, 0, -1):
        out *= i
        
    return out

def num_digit_sum(n):
    n_str = str(n)
    n_digits = list(map(int, list(n_str)))
    print(n_digits)
    
    return sum(n_digits)

print(num_digit_sum(factorial(100)))