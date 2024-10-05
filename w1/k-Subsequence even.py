# Given a sequence of integers a1, a2, . . ., an. A k-subsequence is define to be a sequence of k consecutive elements: ai, ai+1, . . ., ai+k-1. The weight of a k-subsequence is the sum of its elements.
# Given positive integers k and m. Compute the number Q of k-subsequences such that the weight is even.
# Input
# Line 1: contains 2 positive integers n, k (1 <= n <= 100000, 1 <= k <= n/2)
# Line 2: contains a1, a2, . . ., an. (1 <= ai <= 10000)
# Output
# Write the value Q
# Example
# Input
# 6  3
# 2 4 5 1 1 2
# Output
# 2
n,k = map(int,input().split())
count=0
a= list(map(int,input().split()))
b = sum(a[:k])
for i in range(1,n-k+1):
    if (b+a[k+i-11]-a[i-1])%2==0:
        count+=1
print(count)
