#
# Given a sequence of integers a1, a2, ..., an. Perform a sequence of queries over this sequence including:
# find-max: return the maximum element of the given sequence
# find-min: return the minimum element of the given sequence
# sum: return the sum of the elements of the given sequence
# find-max-segment i j: return the maximum element of the subsequence from index i to index j (i <= j)
# Input
# The first block contains the information about the given sequence with the following format:
# Line 1: contains a positive integer n (1 <= n <= 10000)
# Line 2: contains n integers a1, a2, ..., an (-1000 <= ai <= 1000)
# The first block is terminated by a character *
# The second block contains a sequence of queries defined above, each query is in a line. The second block is terminated a 3 characters ***
#
# Output
# Write the result of each query in a corresponding line

input_data = []
input_data.append(input())
input_data.append(input())
while True:
    line = input()
    if line == "***":
        break
    input_data.append(line)

# Parse the sequence
n = int(input_data[0])
sequence = list(map(int, input_data[1].split()))

# Parse the queries
queries = input_data[2:]

# Process the queries
results = []
for query in queries:
    if query == "find-max":
        results.append(max(sequence))
    elif query == "find-min":
        results.append(min(sequence))
    elif query == "sum":
        results.append(sum(sequence))
    elif query.startswith("find-max-segment"):
        _, i, j = query.split()
        i, j = int(i), int(j)
        results.append(max(sequence[i-1:j]))

# Output the results
for result in results:
    print(result)
