# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:25:28 2020

@author: Prital Bamnodkar
"""

def minion_game(string):
    # your code goes here
    sub_string_list = []
    vowels = "aeiou"
    
    print("1")
    for i in range(1, len(string) + 1): #i is the the lenght of substring to find. smallest substrings will be single character, biggest is the string itself
        for j in range(len(string) - i + 1): #loop characters in the string
            sub_string_list.append(string[j: j+i])
            
    #make a dict of elements in the list
    #the keys will be the substrings, and the values will be their frequency in string, use count() function to get their frequency
    sub_dict = {}
    print("2")
    
    for substr in sub_string_list:
        if not substr in sub_dict.keys():
            sub_dict[substr] = string.count(substr)
    
    kevin_score = 0 #the vowels guy
    stuart_score = 0
    
    for key in sub_dict.keys():
        print(key)
        if key[0] in vowels:
            kevin_score += sub_dict[key]
        else:
            stuart_score += sub_dict[key]
            
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Stuart", stuart_score)
    

s = input()
minion_game(s)