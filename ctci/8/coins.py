#!/usr/bin/env python3
""" 8.11 Coins """

count = 0
def coins(n):
    """ Given an infinite number of quarters, dimes, nickels and pennies, compute the possible number of ways to represent
    'n' cents

    Approach:
    """

    global count
    def recurse(m):
        global count
        if m == 0:
            count += 1
        else:
            if m >= 25:
                recurse(m-25)
            if m >= 10:
                recurse(m-10)
            if m >= 5:
                recurse(m-5)
            if m >= 1:
                recurse(m-1)
    recurse(n)
    return count

print(coins(5) == 2)

def coins2(coins, n):
    """ Given a list of unique coin values, compute the least number of total coins needed to represent `n` cents.

    Approach: From the previous problem we realize that we can use recursion to comput the number of possible ways to
    represent 'n' cents with some given coin values. To compute the optimal number coins needed, we can take a min across
    all coin counts of the possible coin representations. We can use dynamic programming to solve this, as we can look at
    the structure of the previous problem. There are a finite number of representations per cent value from [0,n]. Moreso,
    because of the recursive nature of the problem, knowing the optimal number of representations for 'n-1' informs the
    optimal number of representations for 'n', since you know exactly how many coins left are needed to represent the next
    'n' cent value from 'n-1'.
    """

    opt = [0 for _ in range(n)]
    def recurse(m):
        if m < 0: return -1
        if m == 0: return 0
        if opt[m-1] != 0: return opt[m-1]
        else:
            minVal = float('inf')
            for coin in coins:
                # Iterate through each of the coins and check the 'm-coin' optimum. If a new optimum is found, we are now
                # informed for the minimum value for 'm' for when we include 'coin'.
                val = recurse(m-coin)
                if 0 <= val < minVal:
                    minVal = val + 1

            if minVal == float('inf'):
                # No valid representation was found.
                opt[m-1] = -1
            else:
                opt[m-1] = minVal
            return opt[m-1]
    return recurse(n)


print(coins2([1,2,5], 11) == 3)

