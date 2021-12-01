# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:57:14 2021

@author: Prital Bamnodkar
"""

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#     then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
#     how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
#     contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
#     The use of "and" when writing out numbers is in compliance with British usage.

import random, math

def num_to_letters(n):
    # not accurate for n >= 1000 when one or more digit places are 0
    
    digits = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine', 11: 'eleven', 12:'twelve', 13: 'thirteen', 14: 'fourteen', 
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', }
    tens = { 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
             8: 'eighty', 9: 'ninety', }
    orders_of_10 = { 2: 'hundred', 3: 'thousand', }
    
    res = ''
    if n > 20:
        n_expanded = get_expanded_form(n)
        # print('expanded form of', n, 'before splitting into a list:', n_expanded)
        
        n_expanded_broken = list(map(int, (n_expanded.split(' + '))))
        
        # print('expanded form of', n, ':',n_expanded_broken)
    
    # print(n_expanded, n_expanded.split(' + ')
    
    if n < 20 and n != 10:
        res = digits[n]
    elif n < 100 and n % 10 == 0:
        res = tens[n // 10]
    elif is_power_10(n) or n % 100 == 0:
        order = int(math.log10(n))
        res = res + num_to_letters(n // (10 ** order)) + ' ' + orders_of_10[order]
    elif n < 100:
        res = num_to_letters(n_expanded_broken[0]) + '-' + num_to_letters(n_expanded_broken[1])
    elif len(n_expanded_broken) == 2:
        try:
            res = num_to_letters(n_expanded_broken[0]) + ' and ' + num_to_letters(n_expanded_broken[1])
        except:
            print('error!...for:', n, 'with expanded form:', n_expanded_broken)
    else:
        for digit in n_expanded_broken[:len(n_expanded_broken) - 2]:
            order = int(math.log10(digit))
            
            res = res + num_to_letters(digit // 10**order) + ' ' + orders_of_10[order] + ' '
        
        # last two digits use a little different wording
        res = res + 'and ' + num_to_letters(sum(n_expanded_broken[-2:]))
        
    return res

def num_to_letters_ranged(start, n):
    out = []
    
    for num in range(start, n):
        out.append(num_to_letters(num))
        
    return out

def count_letters(num_letters_list):
    count = 0
    
    for num in num_letters_list:
        num_copy = num[:]
        
        num_copy = num_copy.replace(' ', '')
        num_copy = num_copy.replace('-', '')
        
        # print('--', num, ' : ',  num_copy)
        
        count += len(num_copy)
        
    return count

def get_expanded_form(n):
    res = []
    n_str = str(n)
    n_str_reversed = n_str[::-1]
    
    for i in range(len(n_str)):
        try:
            digit = int(n_str_reversed[i])
        except:
            print('error explanding ...', 'n_str:', n_str,' n_str_reversed:', n_str_reversed, ' i:', i)
        
        if digit == 0:
            continue
        
        # print('--',i)
        res.append(str(digit * 10**i))

    return ' + '.join(reversed(res))

def is_power_10(n):
    order = math.log10(n)
    
    if math.ceil(order) == math.floor(order):
        return True
    return False
        
def test_num_to_letters():
    test_cases = list(random.randrange(1000) for x in range(10)) + [1000, 10, 40, 300, 900, 500]
    print('test cases:', test_cases)
    
    print('testing num_to_letters.....')
    for test_case in test_cases:
        print('test case:', test_case)
        print('output:', num_to_letters(test_case), '\n')

def test_get_expanded_form():
    test_cases = list(random.randrange(100000) for i in range(10))
    
    print('testing get_expanded_form.......')
    for test_case in test_cases:
        print('\t', test_case, ':', get_expanded_form(test_case))
    print('testing completed.')

# test_num_to_letters()
# print(num_to_letters(1001))
# test_get_expanded_form()

# print(num_to_letters_ranged(31))
print(count_letters(num_to_letters_ranged(1, 1001)))