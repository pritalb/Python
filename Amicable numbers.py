# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:04:01 2021

@author: Prital Bamnodkar
"""

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from prime_efficient import divisors

def amicable_pairs_less_than(n):
    # returns a list of all amicable pairs less than 10000
    out = []
    
    for i in range(1, n):
        pairs = amicable_pair(i)
        if i not in out and pairs and pairs[0] < n and pairs[1] < n:
                out += pairs
    return out

def amicable_pair(n):
    n_divisors = divisors(n)[:-1]
    pair = sum(n_divisors)
    
    pair_divisors_sum = sum(divisors(pair)[:-1])
    
    if n == pair_divisors_sum and n != pair:
        return [n, pair]
    return None

print(sum(amicable_pairs_less_than(10000)))