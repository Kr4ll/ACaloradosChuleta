# A utility function to multiply two 
# matrices a[][] and b[][]. Multiplication 
# result is stored back in b[][]
def multiply(a, b):
    # Creating an auxiliary matrix 
    # to store elements of the
    # multiplication matrix
    mul = [[0 for x in range(3)]
              for y in range(3)];
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0;
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j];
    # storing the multiplication
    # result in a[][]
    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]; # Updating our matrix
    return a;

def power(F, n):
    M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]];
    # Multiply it with initial values i.e 
    # with F(0) = 0, F(1) = 1, F(2) = 1
    if (n == 1):
        return F[0][0] + F[0][1];
    power(F, int(n / 2));
    F = multiply(F, F);
    if (n % 2 != 0):
        F = multiply(F, M);
    # Multiply it with initial values i.e 
    # with F(0) = 0, F(1) = 1, F(2) = 1
    return F[0][0] + F[0][1] ;
