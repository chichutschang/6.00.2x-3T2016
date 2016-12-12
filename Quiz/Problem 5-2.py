# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:26:53 2016

@author: chi-chu tschang
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    max_so_far = 0
    max_end = 0
    
    for i in range(0, len(L)):
        max_end = max_end + L[i]
        if max_end < 0:
            max_end = 0
        elif (max_so_far < max_end):
            max_so_far = max_end
            
    return max_so_far