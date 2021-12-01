# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:26:57 2021

@author: Prital Bamnodkar
"""

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

print(sum(list(map(int, list(str(2**1000))))))