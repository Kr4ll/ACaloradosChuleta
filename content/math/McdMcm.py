# Python program to demonstrate working of extended
# Euclidean Algorithm
# Alternativa usar el inbuilt de math.gcd()
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a // gcdExtended(a,b))* b 
