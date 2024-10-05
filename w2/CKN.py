# Given two positive integers k and n. Compute C(k,n) which is the number of ways to select k objects from a given set of n objects.
# Input
# Line 1: two positive integers k and n (1 <= k,n <= 999)
# Output
# Write te value C(k,n) modulo 10
# 9
# +7.
# Example
# Input
# 3  5
# Output
# 10
# PYTHON
def binomial_coefficient(k, n, mod=10 ** 9 + 7):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Calculate factorials and their modular inverses
    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = factorial[i - 1] * i % mod

    def mod_inverse(x, mod):
        return pow(x, mod - 2, mod)

    # Calculate the binomial coefficient
    result = (factorial[n] * mod_inverse(factorial[k], mod) % mod * mod_inverse(factorial[n - k], mod) % mod) % mod
    return result


k, n = map(int, input().split())
print(binomial_coefficient(k, n))
