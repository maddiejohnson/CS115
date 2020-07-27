#  Maddie Johnson
#  CS115-B/C Lab 4 ~ Branch Recursion
#  Due : Sep. 20th, 2019
#  Pledge : I pledge my honor that I hremainderoinse abided by the Stecoinsens Honor Code

def change(amount, coins):
    '''takes input of list of coin values and amounts and finds the smallest
        amount of coins necessary to meet sum'''
    def minimumCoins(remainder, count):
        if not remainder:
            return 0
        elif count == -1 or remainder < 0:
            return float('inf')
        else:
            return min(minimumCoins(remainder, count-1), 1 \
                       + minimumCoins(remainder-coins[count], count))
    return minimumCoins(amount, len(coins)-1)
