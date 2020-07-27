'''
Name: Maddie Johnson

Date: 10/4/2019

CS115 - Lab 6 ~ Binary

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

# Given an integer >= 0, convert it to the R2L binary format.
# Take note that either [] or [0] can be used to represent 0 in R2L
def decimalToBinary(x):
    if x == 0:
        return []
    quotient = x//2
    remainder = x%2
    if quotient == 0:
        return [remainder]
    else:
        return [remainder] + decimalToBinary(quotient)

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
    if num == [] or 0:
        return 0
    else:
        end = len(num)-1
        return (2**end)*num[end] \
               + binaryToDecimal(num[:end])

# Given an R2L formatted number, return an R2L equivalent to one more than num
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
    if num == [] or 0:
        return 0
    return decimalToBinary(binaryToDecimal(num)+1)

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
## We will know.
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
def addBinary(num1, num2):
    if len(num1) < len(num2):
        num1 = num1 + ([0]*(len(num2)-len(num1)))
    if len(num1) > len(num2):
        num2 += [0]*(len(num1)-len(num2))
    def helper(num1, num2, carry):
        '''accounts for carry when num1[0] and num2[0] == 1'''
        if carry == 1 and len(num1) == 0 and len(num2) == 0:
            return [1]
        elif carry == 0 and len(num1) == 0 and len(num2) == 0:
            return []
        temp = num1[0] + num2[0] + carry
        if temp == 0:
            return [0] + helper(num1[1:], num2[1:],0)
        if temp == 1:
            return [1] + helper(num1[1:], num2[1:],0)
        if temp == 2:
            return [0] + helper(num1[1:], num2[1:],1)
        if temp == 3:
            return [1] + helper(num1[1:], num2[1:],1)
    return helper(num1, num2, 0)










    
    
        
    
