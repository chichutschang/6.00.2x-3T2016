# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:33:25 2016

@author: chi-chu tschang
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:20:10 2016

@author: chi-chu tschang
"""
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<'+self.name+', '+ str(self.value)+' , '+ str(self.weight)+'>'
        return result
    
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase','book', 'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10,9,4,2,1,20]
    Items =[]
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    return Items


def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags whereby each 
    item is in one or zero bags.
    
    Yields a tuple, (bag1, bag2), where each bag is represented as
    a list of which item(s) are in each bag.
    """
    N = len(items)
    #enumerate the 3**N possible combinations
    for i in range(2**N):
        bag1 = []
        bag2 = []
        #print ('i: ', i)
        for j in range(N):
        #print ('j: ', j)
            if (i /(3**j)) % 3 == 1:
                bag1.append(items[j])
                #yield bag1
            #print('bag 1:' , bag1)
            elif(i / (3**j)) % 3 == 2:
                bag2.append(items[j])
                #yield bag2
            #print('bag 2:' , bag2)
    yield(bag1, bag2)
            
items = buildItems()
combos = yieldAllCombos(items)
for k1, k2 in combos:
    for ka, kb in zip(k1, k2):
        return(ka, kb)