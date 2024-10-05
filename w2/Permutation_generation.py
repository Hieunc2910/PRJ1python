# Given an integer n, write a program to generate all permutations of 1, 2, ..., n in a lexicalgraphic order (elements of a permutation are separated by a SPACE character).
# Example
# Input
# 3
# Output
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
from itertools import permutations
def permute(n):
    for p in permutations(range(1, n + 1)):
        print(' '.join(map(str, p)))

n = int(input())

permute(n)