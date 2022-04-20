# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:30:37 2021

@author: Prital Bamnodkar
"""

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from prime_efficient import get_primes_less_than

def prime_sum(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    Int.
        Sum of all primes below n

    '''
    primes = get_primes_less_than(n)
    return sum(primes)
        
    
x = 2000000
print(x)
print(prime_sum(x))