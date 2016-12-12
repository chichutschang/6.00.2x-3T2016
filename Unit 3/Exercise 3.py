# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:36:20 2016

@author: chi-chu tschang
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
        
    if len(L) == 0:
        return float('NaN')
        
    #compute mean
    value = 0
    for s in L:
        value += len(s)
        print(value)
    mean = value /len(L)
    
    #compute variance
    devSquared = 0
    for s in L:
        devSquared += (len(s) - mean)**2
    variance = devSquared / len(L)
    
    stdDev = variance**(0.5)
    return stdDev
    
#use a separate function for std dev
def stdDev(X):
    mean = sum(X) / len(X)
    total = 0.0
    for x in X:
        total += (x - mean)**2
    return (total/len(X))**0.5
    
def stdDevOfLengths(L):
    n = len(L)
    if (n==0):
        return float('NaN')
    X=[]
    for s in L:
        X.append(len(s))
    return stdDev(X)