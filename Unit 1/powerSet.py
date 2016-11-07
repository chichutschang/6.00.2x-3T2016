# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:12:16 2016

@author: chi-chu tschang
"""

#generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            #test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            yield combo
        