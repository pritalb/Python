# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:01:39 2021

@author: Prital Bamnodkar
"""
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from largest_prime_factor import unique_factors

def is_prime(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    Bool.
        True if n is prime, else False.

    '''
    factors_list = unique_factors(n)
    # print(factors_list)
    
    if len(factors_list) == 2 and factors_list[-1] == n:
        return True
    return False

def n_primes(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    List.
        a list first n primes

    '''
    primes = []
    
    i = 2
    while True:
        if len(primes) > n:
            break
            
        if is_prime(i):
            primes.append(i)
        
        i += 1
        
    return primes

def nth_prime(n):
    '''

    Parameters
    ----------
    n : Int

    Returns
    -------
    Int.
        nth prime number

    '''
    return n_primes(n)[-1]

    

# ls = n_primes(10)
# print(ls, '\n', len(ls))