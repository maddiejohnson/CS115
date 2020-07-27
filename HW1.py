############################################################
#
#  Maddie Johnson
#
#  CS115-B/C HW1 ~ Applications of Map & Reduce
#
#  Due : Sep. 20th, 2019
#
#  Pledge : I pledge my honor that I have abided by the Stevens Honor Code
# 
############################################################


from functools import reduce
from math import factorial, sqrt # this import is necessary to use sqrt and factorial.

def taylorApproxE(lastIter):
    ''' computes approximation of e using the taylor series. The user determines how
    many terms are used in the summation and the approximation is outputted'''
    def taylor(x):
        return 1/factorial(x)
    L = list(map(taylor, range(lastIter+1)))
    return reduce(add, L)

def add(x,y):
    '''computes sum of two given variables x and y'''
    return x + y

def square(x):
    '''takes value and returns the square of the value'''
    return x*x


def vectorNorm(vect1):
    '''takes an inputted list and returns the square root of the sum of the squares
    also known as the vectorNorm'''
    vect1 = list(map(square, vect1))
    return sqrt(reduce(add, vect1))


def arithMean(vect1):
    '''takes inputted list and outputs the arithmetic mean. The sum
    of the list is calculated and then divided by its length'''
    return reduce(add, vect1)/len(vect1)



