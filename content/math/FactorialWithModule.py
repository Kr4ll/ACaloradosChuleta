def factorial(n) :
    M = 1000000007
    f = 1
 
    for i in range(1, n + 1): 
        f = (f * i) % M # Now f never can 
                        # exceed 10^9+7 
 
    return f 
