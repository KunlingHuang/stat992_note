#!/usr/bin/env python

def logfactorial(n, k = 0):
    """
    Calculates log(n!), where n should be a non-negative integer
    Examples:

    >>> logfactorial(1)
    0.0
    
    >>> logfactorial(5,3)
    2.995732273553991
    
    >>> logfactorial(5,5)
    0
    
    >>> logfactorial(5,6)
    0
    """
    #checks on the input n
    assert int(n) == n and n >= 0, 'Warning: input n should be a non-negative integer.'
    assert int(k) == k and k >= 0, 'Warning: input k should be a non-negative integer.'
    if (k >= n):
        return 0
    
    sum = 0
    for i in range(k+1,n+1):
        sum += math.log(i)
        
    return sum

def choose(n, k, log = False):
    """
    usage: choose(n,k)
    Examples:

    >>> choose(5,3)
    10.0
    """
    result = logfactorial(n, k) - logfactorial(n-k)
    if (log == True):
        return result
    
    return round(np.exp(result))


def runTests():
    print("testing the module...")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    import argparse
    import doctest
    import math
    import numpy as np
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "-N", type=int, help="total number of items to choose from")
    parser.add_argument("-k", "-K", type=int, help="number of items to choose")
    parser.add_argument("-l", "--log", action="store_true", help="returns the log binomial coefficient")
    parser.add_argument("--test", action="store_true", help="tests the module and quits")
    args = parser.parse_args()
    if args.test:
        runTests()
    elif (args.log):
        print(format(choose(args.n, args.k, args.log), '.13f'))
    else:
        print(format(choose(args.n, args.k), '.0f'))

    
    
    

