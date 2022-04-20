# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:49:53 2021

@author: Prital Bamnodkar
"""

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def Squares_less_than(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    Dict.
        a dictionary of first n squares
    '''
    squares = {}
    
    for i in range(1, n + 1):
        squares[i] = i**2
    
    return squares

def Pythagorean_triplets(n):
    '''

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    list.
        a list of tuples of pythagorean triplets less than n

    '''
    squares_dict = Squares_less_than(n)
    square_roots = list(squares_dict.keys())
    result = []
    
    for i in square_roots:
        for j in square_roots[square_roots.index(i):]:
            c = squares_dict[i] + squares_dict[j]
            
            if squares_dict[i] + squares_dict[j] in squares_dict.values():
                result.append((i, j, int(math.sqrt(c)))) # sqrt() returns a float, so typecasted it to an int for peace of mind
        
    return result

def Special_triplet(n):
    '''

    Parameters
    ----------
    n : Int
        DESCRIPTION.

    Returns
    -------
    Tuple.
        a tuple of pythagorean triplets a, b, and c such that a + b + c = n
    '''
    
    triplets = Pythagorean_triplets(n)
    
    for triplet in triplets:
        if sum(triplet) == n:
            return triplet
        
    return None

print(Special_triplet(1000))