'''
Name: Maddie Johnson

Date: 9/27/2019

CS115 - HW 2 ~ Recursion

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

## Part 1 ~ Change

def makeChange(val, coins):
    '''takes input of list of coin values and amounts and finds the smallest
        amount of coins necessary to meet sum. Outputs list of coins to meet sum
        and how many coins'''
    if val == 0:
        return [0,[]]
    if coins == [] or val < 0:
        return [float('inf'),[]]
    else:
        loseIt = makeChange(val,coins[1:])
        useIt = makeChange(val-coins[0],coins)
        if useIt[0] < loseIt[0]:
            return [useIt[0] + 1, useIt[1] + [coins[0]]] #returns as list
        else:
            return loseIt
        
            

## Part 2 ~ Least Common Substrings

def LCS(a, b):
    '''takes strings a and b and returns the longest common string'''
    if not a or not b:
        return ''
    if a[0] == b[0]:
        return a[0] + LCS(a[1:], b[1:])  #returns substring if in common
    else:
        return max(LCS(a, b[1:]), LCS(a[1:], b), key=len)  #maximizes common string

def PLCS(a, b):
    '''uses LCS to find the longest common substring and calls compareString to
    return the indices for each character of the LCS'''
    commonString = LCS(a, b)
    if commonString == '':
        return [[-1],[-1]]  #if there is no LCS
    else:
        return [compareString(commonString, a, 0), compareString(commonString, b, 0)]


def compareString(s1, s2, count):
    '''compares the strings from PLCS and returns the indices'''
    if not s2:
        return []
    if not s1:
        return []  #checks if empty
    elif s1[0] == s2[0]:
        return [count] + compareString(s1[1:], s2[1:], count + 1)  #returns count (index) if in common
    else:
        return compareString(s1, s2[1:], count + 1)  #splices s2 if no indexes in common with s1
    
    





