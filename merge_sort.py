# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:39:12 2022

@author: Prital Bamnodkar
"""

def MergeSort(a_list):
    if len(a_list) == 1:
        return a_list
    else:
        n = len(a_list)
        l1 = a_list[: n//2]
        l2 = a_list[n//2 :]
        res = []
        
        l1_sorted = MergeSort(l1)
        l2_sorted = MergeSort(l2)
        
        while len(res) < n:
            if len(l1_sorted) == 0:
                res = res + l2_sorted
            elif len(l2_sorted) == 0:
                res = res + l1_sorted
            else:
                l1_first_elem = l1_sorted[0]
                l2_first_elem = l2_sorted[0]
                
                if l1_first_elem < l2_first_elem:
                    res.append(l1_first_elem)
                    l1_sorted.remove(l1_first_elem)
                else:
                    res.append(l2_first_elem)
                    l2_sorted.remove(l2_first_elem)
        return res
    
if __name__ == '__main__':
    l = [3, 2, 4, 1, 78, 21, 0, 1, 1]
    print(MergeSort(l))