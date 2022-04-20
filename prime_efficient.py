# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:51:58 2021

@author: Prital Bamnodkar
"""

import math

def is_prime(n):
    # prime function using memoization
    # a number is prime if it not divisible by all primes smaller than itself
    
    primes = get_primes()
    
    if n in primes:
        return True
    
    primes = primes_less_than(n, primes)
    
    for prime in primes:
        if n % prime == 0:
            return False
    
    set_prime(n)
    return True
    
    

def get_primes():
    '''
    Returns
    -------
    List.
        Returns a list of prime numbers stored in the file primes.txt
    '''
    
    f = open('primes.txt', 'r')
    res = []
    
    for prime in f.readlines():
        res.append(int(prime))
        
    f.close()
    return res

def set_prime(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.
            Append the number n to the file primes.txt
    Returns
    -------
    None.

    '''
    with open('primes.txt', 'r') as file:
        if str(n) in file.readlines():
            print('prime already known:', n)
            return
    
    f = open('primes.txt', 'a')
    f.write(str(n)+'\n')
    f.close()

def n_primes2(n, primes):
    # Returns a list of first n primes, primes -> list of primes known
    
    max_prime_known = max(primes)
    primes_known = len(primes)
    
    if n < primes_known:
        return primes[:n]
    
    i = max_prime_known
    while len(primes) < n:
        if is_prime(i) and i not in primes:
            set_prime(i)
            primes.append(i)
        i += 1
        
    return primes

def primes_less_than(n, primes_list):
    # return a list of all primes less than n
    # primes_list: a list of all known primes
    
    
    # we will work on a copy of the primes list to avoid any unwanted mutation
    primes = primes_list[:]
    
    primes_known = len(primes)
    max_num_known = get_max_num_encountered()
  
    if n == max_num_known or n == max_num_known + 1:
        return primes[:primes_known]
    elif n < max_num_known:
        res = []
        for prime in primes:
            if prime >= n:
                return res
            res.append(int(prime))
    
    new_numbers = num_in_range(max_num_known + 1, n)
    
    # we need to iterate through all numbers from the smallest known prime, i.e. 2, to n
    # we just add the new numbers to known primes instead of using range(2, n) to avoid repetitive work since we already know the starting primes
    primes = primes + new_numbers
    
    index = 0
    while index < len(primes):
        prime = primes[index]
        
        if prime ** 2 > n:
            # for prime == 2, you dont need to go beyond n/2 since we already got rid of all multiples of 2:
            # same for 3, after we get rid of all multiples of 3, we dont need to look after n/3 and up, since 3 * (any number > n/3) would be bigger than n and thus out of our range
            # carry this on and we learn that after getting rid of all multiples of a number 'i', we dont need to look after any number greater than n/i
            # some more exploration and we find that we can stop the loop at a number whose square is greater than n
            print('breaking because', prime, '**2:', prime ** 2, '>', n, '\n---\n\n')
            break
        
        # get all multiples of prime in range prime + 1 to n, we use prime + 1 instead of prime because we dont want to get rid of the prime number itself
        multiples = multiples_in_list(prime, primes[primes.index(prime) + 1:])
        primes = Diff(primes, multiples)
        primes.sort()        
        index += 1
            
    
    # get the new primes and add them to our file containing known primes
    new_primes = primes[primes_known:]
    set_prime_multiple(new_primes)
            
    if n - 1 > max_num_known:
        set_max_num_encountered(n - 1) # because we only checked number less than n
        
    return primes
    
def get_n_primes(n):
    primes = get_primes()
    
    return n_primes2(n, primes)

def get_primes_less_than(n):
    primes = get_primes()
    
    return primes_less_than(n, primes)

def get_max_num_encountered():
    f = open('max_num_encountered.txt', 'r')
    
    num = int(f.read())
    
    f.close()
    
    return num

def set_max_num_encountered(n):
    f = open('max_num_encountered.txt', 'w')
    
    f.write(str(n))
    
    f.close()
    
def num_in_range(i, n):
    # return a list of numbers in range i to n (exclusive)
    res = []
    
    for j in range(i, n):
        res.append(j)
        
    return res

def multiples_in_list(n, ls):
    # return a list of all multiples of n in the list ls
    res = []
    
    for k in ls:
        if k % n == 0:
            res.append(k)
            
    return res

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def set_prime_multiple(ls):
    # add a list of primes to the primes.txt file
    with open('primes.txt', 'a') as file:
        for prime in ls:
            file.write(str(prime) + '\n')
            
def divisors(n):
    divs = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            
            if n // i not in divs:
                divs.append(n//i)
    divs.sort()    
    return divs