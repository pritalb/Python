# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:40:51 2021

@author: Prital Bamnodkar
"""

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#  containing over five-thousand first names, begin by sorting it into alphabetical order.
#  Then working out the alphabetical value for each name, multiply this value by its 
#  alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth
#  3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a
#  score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def word_score(word):
    word_copy = word.lower()
    
    letter_scores = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
    out = 0
    
    for letter in word_copy:
        try:
            out += letter_scores[letter]
        except:
            print('--error', 'ignored', letter, 'since its not a letter.')
        
    return out

def names_score():
    file = open('names.txt', 'r')
    out = 0
    
    names = file.read()
    names = names.split('","')
    
    names.sort()
    
    # the first word of the file is "MARY", when we split the file data into a list,
    # we use split with arguments '","' since the first word has " and not ",", that first " wasnt removed
    # making the first name of the list "MARY, so we manually remove the extra "
    names[0] = names[0][1:]
    
    names.sort()
    
    for name in names:
        try:
            out += (word_score(name) * (names.index(name) + 1))
        except:
            print('--error', 'for input:', name)
    
    return out
    
print(names_score())