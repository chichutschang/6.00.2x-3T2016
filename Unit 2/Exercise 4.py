# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:13:16 2016

@author: chi-chu tschang
"""

import random
def dist1():
    return random.random() * 2 -1
    
def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

def dist3():
    return int(random.random()*10)

def dist4():
    return random.randrange(0,10)
    
def dist5():
    return int(random.random()*10)

def dist6():
    return random.randint(0,10)