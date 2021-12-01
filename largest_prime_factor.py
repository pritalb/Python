# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:39:23 2021

@author: Prital
"""
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

factors_list = []

n = 600851475143

def factors(n):
    # print("--------", n)
    # print('\t--calculating factors of', n, end=" ")
    num = n
    i = 1
    res = []
    
    while num >= i:
        # print('\t*', num, i)
        if num % i == 0:
            res.append(i)
            num = num // i
            # if num not in res:
            #     res.append(num) 
            
        if num % i != 0 or i == 1:
            i += 1
        
    # print('--factors:', res)
    return res

def divisors(n):
    fact = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            fact.append(i)
            
    return fact
        

def unique_factors(n):
    fact_list = factors(n)
    res = []
    
    for factor in fact_list:
        if factor not in res:
            res.append(factor)
            
    # print('\tunique factors: ', res)
    return res
    
def prime_factors(n):
    
    factors_list = unique_factors(n)
    res = []
    
    # print("\t--prime_factors running for value", n, 'with factors', factors_list)
    
    for factor in factors_list:
        f_lst = factors(factor)
        # print('--factor', factor, factors(factor))        
        if len(f_lst) == 2 and f_lst[-1] == factor:
            res.append(factor)
    
    return res

def max_prime_factor(n):
    return max(prime_factors(n))
        
# for test in [2, 16, 78, 39, 13, 31, 100, 1641, 141233]:
#     print('##', test, ':')
#     print('\t', '--prime factors--', prime_factors(test))

# print(divisors(100))

# print('biggest prime factor of', n, 'is', max_prime_factor(n))