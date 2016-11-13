# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:09:08 2016

@author: chi-chu tschang
"""

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    return random.randrange(9,21, 2) +1