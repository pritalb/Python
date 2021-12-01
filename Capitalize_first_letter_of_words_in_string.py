# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:21:22 2020

@author: Prital Bamnodkar
"""
def solve(s):
    res = ""
    s_word_list = s.split()
    
    for word in s_word_list:
        if len(word) > 1:
            res = res + word[0].upper() + word[1:]
        else:
            res = res + word.upper()

    for i in range(len(s)):
        if s[i] == " ":
            res = res[:i] + " " + res[i:]
        
    return res

print(solve("q w e r t y u i o p a s d f g h j    k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"))