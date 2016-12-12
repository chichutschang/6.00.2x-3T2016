# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:37:04 2016

@author: chi-chu tschang
"""

import random
def oneTrial():
    dice =['1','2','3','4','5','6']
    roll = []
    for i in range(3):
    #for three trials, pick a ball
        die = random.choice(dice)
        print(die)
        #remove the chosen ball 
        #balls.remove(ball)
        #add it to balls
        roll.append(die)
    if roll[0] == 6 and roll[1] == 6 or roll[2] == 6 or roll[1] == 6 and roll[2] == 6:
        return True
    return False
        
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue+=1
    return float(numTrue)/float(numTrials)