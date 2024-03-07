# Euler Totient Function
# Return the count of numbers in {1, 2, 3, …, n-1} that are relatively prime to n,
# i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
