# Given an integer n, write a program that generates all the binary sequences of length n in a lexicographic order.
# Input
# Line 1: contains an integer n (1 <= n <= 20)
# Output
# Write binary sequences in a lexicographic ordder, eac sequence in a line
#
# Example
# Input
# 3
# Output
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
n = int(input())
for i in range (2**n):
    print(format(i,'0'+str(n)+'b'))
# Binary sequences generation without consecutive 11
# n = int(input())
# for i in range (2**n):
#     b_o = format(i,'0' +str(n) +'b')
#     if '11' not in b_o:
#         print(b_o)