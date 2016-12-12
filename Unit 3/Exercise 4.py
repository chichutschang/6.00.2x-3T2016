# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:04:15 2016

@author: chi-chu tschang
"""
import random
def oneTrial():
    balls =['r','r','r','g','g','g']
    chosenBall = []
    for i in range(3):
    #for three trials, pick a ball
        ball = random.choice(balls)
        #remove the chosen ball 
        balls.remove(ball)
        #add it to balls
        chosenBall.append(ball)
    if chosenBall[0] == chosenBall[1] and chosenBall[1] == chosenBall[2]:
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