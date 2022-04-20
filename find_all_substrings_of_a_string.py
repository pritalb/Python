# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:17:33 2020

@author: Prital Bamnodkar
"""


# After solving the problem on hackerRank,
# you dont need to create a frequency dict of all substrings

# For the word "BANANA", the first vowel 'A' occurs at position 1,
# len("BANANA") = 6, so there are 6-1 = 5 substrings starting with this letter 'A': 
# ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], you add one extra letter to that specific 
# letter 'A' until you get to the end of the word.

# so you would already know how many substrings start with a consonant or not
def minion_game(string):
    #your code goes here
    vowels = "AEIOU"
    
    kevin_score = 0 #the vowels guy
    stuart_score = 0
            
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


#below is the old solution of the game
def sub_string(string):
    """
    Parameters
    ----------
    string : a string of which substrings are to be found
        DESCRIPTION.

    Returns:
    -------
    a list of all substrings of the string 

    """
    sub_string_dict = {}
    
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = string[i: i + j]
            if key not in sub_string_dict.keys():
                sub_string_dict[key] = 1
            else:
                sub_string_dict[key] += 1    
    return sub_string_dict

def count_substring_frequency(string, substring_list):
    """

    Parameters
    ----------
    string : str
        DESCRIPTION.
        the main string
    substring_list : list
        DESCRIPTION.
        list of all substrings of string

    Returns
    -------
    a tuple of the substring with the highest frequency and its frequency

    """
    
    #make a dict of elements in the list
    #the keys will be the substrings, and the values will be their frequency in string, use count() function to get their frequency
    sub_dict = {}
    max_frequency_subs = []
    
    for substr in substring_list:
        if not substr in sub_dict.keys():
            sub_dict[substr] = string.count(substr)
            
    for key in sub_dict.keys():
        if sub_dict[key] == max(sub_dict.values()):
            max_frequency_subs.append(key)
    if len(max_frequency_subs) == 1:
        return (max_frequency_subs[0], sub_dict[max_frequency_subs[0]])
    return (max_frequency_subs, max(sub_dict.values()))

def minion(string):
    # Kevin and Stuart want to play the 'The Minion Game'.

    # Game Rules
    
    # Both players are given the same string.
    # Both players have to make substrings using the letters of the string.
    # Stuart has to make words starting with consonants.
    # Kevin has to make words starting with vowels.
    # The game ends when both players have made all possible substrings.
    
    # Scoring
    # A player gets +1 point for each occurrence of the substring in the string.
    
    sub_dict = sub_string(string)
    vowels = "AEIOUaeiou"
            
    kevin_score = 0 #the vowels guy
    stuart_score = 0
    
    for key in sub_dict.keys():
        if key[0] in vowels:
            kevin_score += sub_dict[key]
        else:
            stuart_score += sub_dict[key]
            
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
            
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count
    
    
# string = "BAANANAS"
# string = "BANANA"
string = "BFEREZKMEYKTNZZTCVZRWZSIIRLEUWGXROAHKCRZNZKUUFWEDJVPMGNGDVHNIGUNKDAUFOIYXVMVBNBMLDQAYJSXNJFVZCERKWJXYUHHLYEBBVRQTXJMGVNFKYHHPZGZOLIBDNTHTZPDJNASKAQPCTXETRZBGIPYHZHOUJPBPRCEKTOWENMEHJVEPPKQISJLTWQOLATVIFOBEXUJPMKXGUDFHBEGMFCCUXBJMXFOKRCICSPQQFFJZTIHMLURFCCVZYIPYGDTJXGXSUAHOKLVYFMSHOSMNNIIRAUPFAAOQHLQCTUGCMCQMOQUXMYBQXJVYRIIQENPTMBYVOVPFYDOJKVUWKDHDWYNVDAMUBBPNTEZZSDADELGNILAZTTMUMWGKXPSQDYVTGXWGDLAZQIJADPTFIJSLIDTLEJFJGWMOCPYLAFMVHQHRLGSIQJXQQKJAVBMFKEENTJZWBDTDVUBZHVTDFCLLETZJRMYMIQYVWWUOIVPGTNZFNTDKBVZKKFDTSQTVSRAADPWIMXEEJHBFRDDDXMOYEHCUHSBWZLHVCKZKUTVWGNTEPYPNGCDMFNKWGARVDMLZJDPIKLWYULIMBOHVOSWZICGZGBKBODQCVIAVTDZQFYLCRWIQBBGMGGERSLPGYASHNYRVVWAVJYASVATKHQNJNYFCUDXKRDNBWHLRIOFVHVFOJQGGAMKNOVDVKJVBRNAIUBZQEBPWKXZUCIRQDRTRGWKTYIJZNBRGQYKOAQCPCRKKXPAAHWLKSJUJZOOIQCSBPDCWHANQPWSIYDBZFCIEWZKYOMMHCHONSOGVMEGGOUKXLGFVOUSIYFFLZAPTLJYWIQVXZZPYVTAOQFQURGULWGFKBYIKJOCSITSBFRIJINCOBHGZRSFYTXFQRFYCIDLXFCASUQAYTHGNBPFTXLUZIXHNXFJIJQABSGNQDOAWXIDSSMLPHHQXYJGVXEJVDVJNCLLBDAYUQFDRGFAAWMAWZZVDAPLHYDU"
minion_game(string)