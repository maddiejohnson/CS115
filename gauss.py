from functools import reduce

def add(x,y):
    return x + y

def gauss(n):
    return reduce(add, range(n+1))


def multiply(x):
    return x*x

def sumOfSquares(n):
    squares = list(map( multiply, range(n+1)))
    return reduce(add,squares )

