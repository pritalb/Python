# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:46:44 2021

@author: Prital Bamnodkar
# """
# The sum of the squares of the first ten natural numbers is 385,

# The square of the sum of the first ten natural numbers is 3025,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2460.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    '''
    
    Parameters
    ----------
    n : Int

    Returns
    -------
    The Sum of Squares of All Numbers upto n.

    '''
    
    sum = 0
    
    for i in range(1, n + 1):
        sum += (i * i)
        
    return sum

def square_of_sum(n):
    '''

    Parameters
    ----------
    n : Int

    Returns
    -------
    The Square of the Sum of all Natural numbers upto n.

    '''
    sum = 0
    
    for i in range(1, n + 1):
        sum += i
        
    return sum * sum

def square_difference(n):
    '''

    Parameters
    ----------
    n : Int.

    Returns
    -------
    The difference between the square of the sum and the sum of the squares.

    '''
    
    return abs(square_of_sum(n) - sum_of_squares(n))

print(square_difference(100))