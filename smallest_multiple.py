# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:41:35 2021

@author: Prital Bamnodkar
"""
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from largest_prime_factor import factors
            
def get_factors_dict(n):
    '''

    Parameters
    ----------
    n : int
        DESCRIPTION.

    Returns
    -------
    fact_dict : dictionary
        DESCRIPTION.
        returns a dictionary of all prime factors of n
        factor -> its frequency in factors of n
        
        e.g. for n = 12,
                12 = 1 * 2 * 2 * 3
                return {1:1, 2:2, 3:1}

    '''
    
    fact_list = factors(n)
    fact_dict = {}
    
    for factor in fact_list:
        if factor not in fact_dict.keys():
            fact_dict[factor] = 1
        else:
            fact_dict[factor] += 1
            
    return fact_dict

def smallest_multiple(n):
    '''
    Return the smallest number evenly divisible by all numbers upto n.

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    res: Int

    '''
    
    # Divisibility:
    #     For a number 'n' to be divisible by a number 'i', 'n' needs to have 'i' in its factors such that i * x = n, where x is another factor of n
    #     e.g. for 100 to be divisible by 10, 100 needs to have 10 in its factors such that 10 * x = 100, where x is another factor of n
        
    #     However, if n has all the factors of 'i' in its composition it will be divisible by 'i'
    #     e.g. to be divisible by 10, a number needs to have 1,2, and 5 in its factors since 1*2*5 = 10
        
        
    # Making a number divisible by another:
    #     For example, take n = 12 and we have to make n divisible by 8
    #         now n = 12 = 1 * 2 * 2 * 3 and 8 = 2 * 2 * 2
            
    #         so, to be divisible by 8, n needs to have  2 * 2 * 2 in its factors, but it only has 2 * 2 in its factors.
    #         So, to make it divisible by 8, we add another '2' in its factors i.e. we multiply n by 2 to get n = 24 which is divisible by 8.
            
    
    res = 1
    res_fact_dict = {}
    
    # Get all numbers from 1 to n
    for i in range(1, n + 1):
        
        # Get the factors of i
        i_fact_dict = get_factors_dict(i)
        
        for factor in i_fact_dict.keys():
            if factor in res_fact_dict.keys():
                if res_fact_dict[factor] < i_fact_dict[factor]:
                    res_fact_dict[factor] = i_fact_dict[factor]
            else:
                res_fact_dict[factor] = 1
    
    for factor in res_fact_dict.keys():
        res *= (factor  ** res_fact_dict[factor])
        
    return res
    

print(smallest_multiple(20))