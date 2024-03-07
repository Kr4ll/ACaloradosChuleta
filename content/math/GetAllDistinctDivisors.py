# Naive method to print all distinct divisors 
def printDivisors(n) : 
    i = 1
    while i <= n : 
        if (n % i==0) : 
            print (i,end=" ") 
        i = i + 1
