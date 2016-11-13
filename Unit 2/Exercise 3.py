# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:55:45 2016

@author: chi-chu tschang
"""

random.seed(9001)
d=random.randint(1,10)
for i in range(random.randint(1,10)):
    if random.randint(1,10) < 7:    
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1,10))
    