'''
Name: Maddie Johnson

Date: 9/26/2019

CS115 - Lab 5 ~ Turtle

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

from turtle import *

def svTree(trunkLength, depth):
    '''Takes inputted length of trunk and amount of branches and creates a
        tree turtle graphics'''
    if depth >= 1:
        forward(trunkLength)
        left(20)
        svTree(trunkLength/2, depth-1) # creates right branch
        right(40)
        svTree(trunkLength/2, depth-1)
        left(20)
        forward(-trunkLength)
    else:
        return
