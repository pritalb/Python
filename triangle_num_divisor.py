# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:19:42 2021

@author: Admin
"""

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

from prime_efficient import divisors

def triangle_num_with_n_divisors(n):
    i = 2
    num = 1
    
    while True:
        print('\n', '-' * 5)
        num = num + i
        divisors_ls = divisors(num)
        print(num, len(divisors_ls))
        
        if len(divisors_ls) >= n:
            return num
        
        i += 1
        
n = 500
print(triangle_num_with_n_divisors(n))