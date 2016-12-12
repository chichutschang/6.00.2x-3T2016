# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:21:15 2016

@author: chi-chu tschang
"""

nodes = []
for i in range(n):
    nodes.append(newNode(i)) # newNode takes one parameter, the number of the node
    
for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)