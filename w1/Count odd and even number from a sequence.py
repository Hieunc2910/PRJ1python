# Given a sequence of integer a1, a2, ..., an. Count the number of odd elements and even elements of the sequence.
# Input
# Line 1: contains a positive integer n (1 <= n <= 100000)
# Line 2: contains a1, a2, ..., an. (1 <= ai <= 1000000)
# Output
# Write the number of odd elements and the number of even elements (separated by a SPACE character)
#
# Example
# Input
# 6
# 2 3 4 3 7 1
# Output
# 4 2
import sys
input_data = sys.stdin.read().split("\n")
sq= input_data[1].split()
odd = 0
even = 0
for i in sq:
    if int(i)%2 == 0:
        even += 1
    else:
        odd += 1
print(odd,even)