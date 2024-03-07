# Calcular el mod muchas veces, util cuando el divisor es fijo y conocido.
#Time Complexity: O(log b) 
# Calculates (a * b) % mod
def mul_mod(a, b, mod):
    res = 0
    while b > 0:
        if b & 1 == 1:
            res = (res + a) % mod
        a = (a * 2) % mod
        b >>= 1
    return res
# Calculates (a^b) % mod
def pow_mod(a, b, mod):
    res = 1
    a %= mod
    while b > 0:
        if b & 1 == 1:
            res = mul_mod(res, a, mod)
        a = mul_mod(a, a, mod)
        b >>= 1
    return res
# Calculates Barrett reduction of x modulo mod
def barrett_reduce(x, mod, mu):
    r1 = x & 0xFFFFFFFF
    r2 = mu * r1
    q3 = r2 >> 32
    r3 = r1 - q3 * mod
    res = r3 + ((r3 >> 63) & mod)
    if res >= mod:
        res -= mod
    return res
def main():
    x = 123456789
    mod = 1000000007
    mu = ((1 << 64) + mod - 1) // mod
    # Function call
    # Calculate x^2 % mod
    x_squared = mul_mod(x, x, mod)
    x_squared_barrett = barrett_reduce(x_squared, mod, mu)
    print("x^2 % mod =", x_squared_barrett)
    # Calculate x^1234 % mod
    x_pow_1234 = pow_mod(x, 1234, mod)
    x_pow_1234_barrett = barrett_reduce(x_pow_1234, mod, mu)
    print("x^1234 % mod =", x_pow_1234_barrett)
 
