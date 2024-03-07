# Print the least prime factors of numbers
# less than or equal to n using
# modified Sieve of Eratosthenes
def leastPrimeFactor(n) :
    # Create a vector to store least primes.
    # Initialize all entries as 0.
    least_prime = [0] * (n + 1)
    # We need to print 1 for 1.
    least_prime[1] = 1
    for i in range(2, n + 1) :
        # least_prime[i] == 0
        # means it i is prime
        if (least_prime[i] == 0) :
            # marking the prime number
            # as its own lpf
            least_prime[i] = i
            # mark it as a divisor for all its
            # multiples if not already marked
            for j in range(i * i, n + 1, i) :
                if (least_prime[j] == 0) :
                    least_prime[j] = i
    # print least prime factor 
    # of numbers till n
    for i in range(1, n + 1) :
        print("Least Prime factor of "
              ,i , ": " , least_prime[i] )
