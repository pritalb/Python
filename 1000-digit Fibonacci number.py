# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:54:38 2021

@author: Prital Bamnodkar
"""

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def first_fib_to_contain_n_digits(n):
    fib_list = [1, 1]
    
    while len(str(fib_list[-1])) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        
    print('number of digits in out:', len(str(fib_list[-1])))
    print('number of digits in the fib just smaller than n:', len(str(fib_list[-2])))
    return fib_list

print(len(first_fib_to_contain_n_digits(1000)))