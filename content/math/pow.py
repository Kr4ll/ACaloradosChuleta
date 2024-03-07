# Iterative Function to
# calculate (x^y) in O(logy)
def power(x, y):
    # Initialize result
    res = 1
    while (y > 0):
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = res * x
        # y must be even 
        # now y = y/2
        y = y >> 1
        # Change x to x^2
        x = x * x
    return res
