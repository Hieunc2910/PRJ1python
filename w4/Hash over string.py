# Given a string s[1…k] which is a sequence of characters taken from {‘a’, . . ., ‘z’}. Given a positive integer m, the hash code of s is defined by the formula:
# H(s) =  (s[1]*256
# k-1+ s[2]*256
# k-2
#  + . . . + s[k]*256
# 0
# ) mod m  (the contant integer m is a parameter)
# Given a sequence of strings k1, k2, …, kn, compute the corresponding hash codes
# Input
# Line 1: n and m (1 <= n,m <= 100000)
# Line i+1 (i = 1,2,…,n): contains the string ki (the length of each string is less than or equal to 200)
# Output
# Each line contains the corresponding hash code of n given strings
# Example
# Input
# 4 1000
# a
# ab
# abc
# abcd
# Output
# 97
# 930
# 179
# 924
def compute_hash(s, m):
    k = len(s)
    hash_value = 0
    for i in range(k):
        hash_value = (hash_value * 256 + ord(s[i])) % m
    return hash_value
# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
# First line contains n and m
n, m = map(int, data[0].split())
# Process each string and compute its hash code
results = []
for i in range(1, n + 1):
    s = data[i]
    hash_code = compute_hash(s, m)
    results.append(hash_code)
# Print results
for result in results:
    print(result)