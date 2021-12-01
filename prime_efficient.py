# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:51:58 2021

@author: Prital Bamnodkar
"""

import math

# def is_prime(n):
#     '''

#     Parameters
#     ----------
#     n : Int
#         DESCRIPTION.

#     Returns
#     -------
#     Bool.
#         True if n is a prime, else return False.

#     '''
#     # print('function executing')
    
#     if n == 0 or n == 1:
#         return False
#     elif n == 2:
#         return True # default case
    
#     # print('--#n:', n)
#     for i in range(2, n):
#         # print('--', i)
#         if n%i == 0:
#             return False
#     return True

# def n_primes(n):
#     '''

#     Parameters
#     ----------
#     n : Int
#         DESCRIPTION.

#     Returns
#     -------
#     List.
#         a list of first n primes

#     '''
#     primes = []
    
#     i = 2
#     while len(primes) < n:
#         if is_prime(i):
#             primes.append(i)
#             # print(primes, i)
#         i += 1
            
            
#     return primes

def is_prime(n):
    # prime function using memoization
    # a number is prime if it not divisible by all primes smaller than itself
    # print(5 * '___')
    
    # print('\tis_prime called with argument:', n)
    primes = get_primes()
    
    if n in primes:
        return True
    
    # print('\tCalling primes_less_than for argument:', n, 'through is_prime')
    primes = primes_less_than(n, primes)
    
    for prime in primes:
        if n % prime == 0:
            # print('\tn:', n, '%', 'prime:', prime, 'is zero. Returning false')
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

# def primes_less_than(n, primes):
#     # return a list of all primes less than n
    
#     # print('\nprimes_less_than called with n:', n)
    
#     max_prime_known = int(max(primes))
#     primes_known = len(primes)
#     max_num_known = get_max_num_encountered()
#     # print('max_prime_known:', max_prime_known, 'primes_known:', primes_known, 'n:', n)
    
#     if n == max_prime_known:
#         # print('n:', n, '==', 'max_prime_known:', max_prime_known)
#         return primes[:primes_known]
#     elif n < max_prime_known:
#         # print('n:', n, 'is less than max_prime_known:', max_prime_known)
#         res = []
#         for prime in primes:
#             if prime >= n:
#                 # print('returning res:', res)
#                 return res
#             res.append(int(prime))
    
#     # print('Trying to execute loop for:', max_num_known + 1, 'to', n)
#     for i in range(max_num_known + 1, n):
#         # print('\n--', i)
#         if is_prime(i) and i not in primes:
#             print('trying to append', i, 'to primes.')
#             primes.append(i)
#             set_prime(str(i))
            
#     if n - 1 > max_num_known:
#         set_max_num_encountered(n - 1) # because we only checked number less than n
#     return primes

def primes_less_than(n, primes_list):
    # return a list of all primes less than n
    
    # primes_list: a list of all known primes
    
    # print('\nprimes_less_than called with n:', n)
    
    # we will work on a copy of the primes list to avoid any unwanted mutation
    primes = primes_list[:]
    
    primes_known = len(primes)
    max_num_known = get_max_num_encountered()
    # print('max_prime_known:', max_prime_known, 'primes_known:', primes_known, 'n:', n)
    
    if n == max_num_known or n == max_num_known + 1:
        # print('n:', n, '==', 'max_prime_known:', max_prime_known)
        return primes[:primes_known]
    elif n < max_num_known:
        # print('n:', n, 'is less than max_prime_known:', max_prime_known)
        res = []
        for prime in primes:
            if prime >= n:
                # print('returning res:', res)
                return res
            res.append(int(prime))
    
    print('max num known:', max_num_known, 'getting new_numbers,', 'range:', max_num_known + 1, 'to', 'n:', n)
    new_numbers = num_in_range(max_num_known + 1, n)
    
    # we need to iterate through all numbers from the smallest known prime, i.e. 2, to n
    # we just add the new numbers to known primes instead of using range(2, n) to avoid repetitive work since we already know the starting primes
    primes = primes + new_numbers
    # print('primes + new_numbers iterable before the loop:', primes, '\n')
    
    index = 0
    while index < len(primes):
        prime = primes[index]
        # print('-' * 5, 'current prime:', prime, 'index:', index)
        # print('primes before operation:', primes)
        
        if prime ** 2 > n:
            # for prime == 2, you dont need to go beyond n/2 since we already got rid of all multiples of 2:
            # same for 3, after we get rid of all multiples of 3, we dont need to look after n/3 and up, since 3 * (any number > n/3) would be bigger than n and thus out of our range
            # carry this on and we learn that after getting rid of all multiples of a number 'i', we dont need to look after any number greater than n/i
            # some more exploration and we find that we can stop the loop at a number whose square is greater than n
            print('breaking because', prime, '**2:', prime ** 2, '>', n, '\n---\n\n')
            break
        
        # print('removing all multiples of ', prime, ' from range:', max_num_known, 'to', n)
        # get all multiples of prime in range prime + 1 to n, we use prime + 1 instead of prime because we dont want to get rid of the prime number itself
        multiples = multiples_in_list(prime, primes[primes.index(prime) + 1:])
        # print('multiples:', multiples)
        primes = Diff(primes, multiples)
        primes.sort()
        # print('primes after removing multiples:', primes)
        
        index += 1
        # print('\n')
            
    
    # get the new primes and add them to our file containing known primes
    new_primes = primes[primes_known:]
    # print('new_primes:', new_primes)
    set_prime_multiple(new_primes)
            
    if n - 1 > max_num_known:
        print('new highest number: ', n - 1)
        set_max_num_encountered(n - 1) # because we only checked number less than n
    
    print('number of iterations done:', index)
    
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
    # print('setting primes:', ls)
    # add a list of primes to the primes.txt file
    with open('primes.txt', 'a') as file:
        for prime in ls:
            # if str(prime) in file.readlines():
            #     print('prime already known:', prime)
            #     continue
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

# print(set_prime(2))
# print(get_max_num_encountered())
# print(is_prime(535))
# print(get_n_primes(200))
# print('\nAnswer:', get_primes_less_than(2000000))
# print(multiples_in_range(2, 21, 5000000))

# a = list(i for i in range(50))
# b = list(i for i in range(21, 41))
# print(Diff(a, b))

# print(divisors(28))