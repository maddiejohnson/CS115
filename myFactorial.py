def myFactorial(x):
    '''return the factorial of x (assumes x to be a natural number)'''
#    if 0 == x:
#        return 1
#    else:
#        return x * myFactorial(x-1)
    return 1 if not x else x*myFactorial(x-1)


def myLength(L):
#    if L == 0:
#        return 0
#    else:
#        return 1 + myLength(L[1:])
    return 0 if [] == L else 1 + myLength(L[1:])


#def LCS(S1, S2):
#    if 0 == len(S1) or 0 == len (S2):
#        return 0


#def reverse(L):
#    '''computes list in reverse order'''
 #   if not L:
   #     return []
  #  else:
    #    head, tail = L[0],L[1:]
     #   return reverse(tail) + [head]
     
def member(x, L):
    baseVal = False

    def recursiveStep(head, tail):
        return reverse(tail) + [head]

    return baseVal if not L \
       else recursiveStep(L[0], L[1:])


def myMap(f, L):
    '''home-brew version of map'''
    baseVal = []
    
    def recursiveStep(head, tail):
        return [f(head)] + myMap(f, tail)
    
    return baseVal if not L \
           else recursiveStep(L[0], L[1:])


def myReduce(f, L):
    baseVal = L[0]
    def recursiveStep(head, tail):
        print("recursing on " + str(tail))
        return myReduce(f, [f(head, tail[0])] + tail[1:])
    return baseVal if 1 == len(L) \
           else recursiveStep(L[0], L[1:])

def myFilter(f,L):
    baseVal = None

    def recursivePass(head, tail):
        pass
    
    return baseVal if not L \
           else recursiveStep(L[0], L[1:])



def countIf(f,L):
    '''count the number of items in L that satisfy f'''
    return len(list(filter(f, L)))


def myFilter(f,L):
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])


def powerset(S):
    if not S:
        ans = [[]]
    else:
        loseIt = powerset(S[1:])
        useIt = list(map(lambda L: [S[0]] + L, loseIt))
        ans = useIt + loseIt
    return ans

def comb(S,k):
    if not k:
        ans = [[]]
    elif not S:
        ans = []
    else:
        loseIt = comb(S[1:],k)
        useIt = list(map(lambda T: [S[0]] + T, comb (S[1:], k-1)))
        ans = useIt + loseIt

    return ans


from turtle import*

def polygon(sideLength, n):
    angle = 360/n
    def drawSide(k):
        if k > 0:
            forward(sideLength)
            left(angle)
            drawSide(k-1)
    drawSide(n)
    

def snowflake(len, order):
    koch(len, order)
    right(120)
    koch(len, order)
    right(120)
    koch(len, order)
    right(120)

def koch(sideLen, order):
    '''copy from canvas'''
    if 0 == order or 3 > sideLen:
        forward(sideLen)
    else:
        koch(sideLen/3, order-1)
        left(60)
        koch(sideLen/3, order-1)
        left(120)
        koch(sideLen/3, order-1)
        left(60)
        koch(sideLen/3, order-1)
        

