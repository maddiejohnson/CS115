# Maddie Johnson
# 9/6/19
# Convert a list of temps from F to C and compute simple stats

from functools import reduce

def toC(tempF):
    '''convert the given temp from F to C'''
    return(10/18)*(tempF-32)

def toF(tempC):
    '''convert temp from C to F'''
    return (18/10)*tempC + 32

def listToC(l):
    '''convert list of F temps to C temps'''
    return list(map(toC, l))

def tempStats(listF):
    '''convert a list of F temps to C temps adn compute simple stats'''
    def myMin(x, y):
        return x if x < y else y
    
    def myMax(x, y):
        return x if x > y else y
    
    
    
    listC = listToC(listF)
    minTemp = reduce(myMin, listC)
    maxTemp = reduce(myMax, listC)

    return [minTemp, maxTemp, listC]
                
