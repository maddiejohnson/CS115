# I pledge my honor I have abided by the Stevens Honor System
# Maddie Johnson
#
# These functions use recursion to iterate through lists and complete different tasks


def dotProduct(L, K):
    ''' Multiplies the same indexes from two given lists and outputs the sum'''
    if not L or not K:
        return 0
    else:
        return(L[0]*K[0] + dotProduct(L[1:],K[1:]))


def expand(S):
    '''takes a string and returns a list of its characters'''
    if not S:
        return []
    else:
        return [S[0]] + expand(S[1:])


def deepMember(e, L):
    '''takes given list and searches for given target. returns true if element
        is present and false if not'''
    if not L:
        return
    if isinstance(L, range) == False:
        L = flatList(L)
    if e == L[0]:
        return True
    if e != L[0] and myLength(L) == 1:
        return False
    else:
        return  deepMember(e, L[1:])


def removeAll(e, L):
    '''finds a given element of a given list and outputs the list without the element'''
    if not L:
        return L
    if isinstance(L[0],list):
        L[0] = removeAll(e, L[0])
    if e == L[0]:
        return removeAll(e, L[1:])
    if e != L[0]:
        newList = L[0]
        return [newList] + removeAll(e, L[1:])

def deepReverse(L):
    '''returns the reverse string of a given string'''
    if myLength(L) == 1:
        if isinstance(L[0], list):
            return [deepReverse(L[0])]
        else:
            return L
    if myLength(L) == 0:
        return ''
    else:
        return deepReverse(L[1:]) + deepReverse(L[:1])
    

def flatList(L):
    '''takes given list and outputs flat list without nested lists'''
    if not L:
        return L
    if isinstance(L[0], list):
        return flatList(L[0]) + flatList(L[1:])
    return L[:1] + flatList(L[1:])

def myLength(L):
    '''takes given list and outputs length'''
    return 0 if not L else 1 + myLength(L[1:])

