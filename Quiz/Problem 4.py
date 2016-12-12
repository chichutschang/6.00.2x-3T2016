# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:50:17 2016

@author: chi-chu tschang
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if len(L)>0:    
        m = [0 for _ in range(len(L))]
        m[0]  = s // L[0] 
        running_sum = s - L[0]*m[0]
        for i in range(1,len(L)):
            m[i] = running_sum // L[i]        
            running_sum -= m[i]*L[i] 
        if running_sum == 0:
            return(sum(m))     
    return "no solution"