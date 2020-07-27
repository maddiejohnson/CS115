#Maddie Johnson
#9/5/2019
#LL
#I pledge my honor that I have abided by the Stevens Honor System

from functools import reduce

def findLongestWord(string):
    '''makes separate list of string lengths'''
    wordLengths = list(map(len,string))
    '''Finds the max of the wordLengths list and uses the same index to
        return the string in the string list'''
    return string[wordLengths.index(reduce(max,wordLengths))]
    
