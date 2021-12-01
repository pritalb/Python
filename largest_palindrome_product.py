# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:01:38 2021

@author: Prital Bamnodkar
"""

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# to check if a string s is a palindrome,
#     get len(s),
    
#     set i = 0 and j = len(s) - 1
#         check if s[i] == s[j],
#             if yes, i++ and j--:
#             if no, return False:
#         if s[i] != s[j], i.e. the character on nth position from left and the one from right dont match,
#         the s is not a palindrome, 
#             therefore return False

def is_palindrome(s):
    '''
    Parameters
    ----------
    s : TYPE:str
        DESCRIPTION.
        check if a given string is a palindrome

    Returns
    -------
    Bool

    '''
    
    n = len(s)
    
    for i in range(0, n - 1):
        # print('\titeration', i)
        j = n - 1 - i
        # print('\t', s[i], s[j])
        if s[i] == s[j]:
            continue
        else:
            # print('\treturning false for ', i, 'and', j, 'on iteration ', i)
            return False
        
    return True

palindrome_numbers = []

for i in range(999, 1, -1):
    for j in range(i, 1, -1):
        print(i, j, i*j)
        if is_palindrome(str(i * j)):
            palindrome_numbers.append(i*j)
          
print(palindrome_numbers)
print(max(palindrome_numbers))
# for test in ['abba', 'a', 'aba', 'cat', 'abca']:
#     print('#', test)
#     print('\t result:', test, is_palindrome(test))