# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:06:07 2021

@author: Prital Bamnodkar
"""

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#     https://projecteuler.net/project/images/p015.png

# How many such routes are there through a 20×20 grid?

# the number of paths to each node form pascal's triangle
# the total paths to the bottom node of a grid of size nxn are given by the binomial coefficient at (n)th column in the (2n)th row
from math import factorial

def binomial_coefficient(n, k):
    coefficient = factorial(n) / (factorial(k) * factorial(n - k))
    
    return int(coefficient)

def lattice_paths(n):
    row = 2 * n
    col = n
    
    return binomial_coefficient(row, col)

print(lattice_paths(20))