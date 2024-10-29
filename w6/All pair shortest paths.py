# Given a directed graph G = (V, E) in which V = {1, 2, ..., n} is the set of nodes, and w(u,v) is the weight (length) of the arc(u,v). Compute d(u,v) - the length of the shortest path from u to v in G, for all u,v in V.
# Input
# Line 1: contains 2 positive integers n and m (1 <= n,m <= 10000)
# Line i+1 (i = 1, 2, ..., m): contains 3 positive integers u, v, w in which w is the weight of the arc (u,v) (1 <= w <= 1000)
# Output
# Line i (i = 1, 2, ..., n): wirte the ith row of the matrix d (if there is not any path from node i to node j, then d(i,j) = -1)
import sys
input = sys.stdin.read

def floyd_warshall(n, graph):
    # Initialize distance matrix
    d = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0

    # Update distance matrix with input weights
    for u, v, w in graph:
        d[u-1][v-1] = w

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # Replace infinity with -1 for no path
    for i in range(n):
        for j in range(n):
            if d[i][j] == float('inf'):
                d[i][j] = -1

    return d

def main():
    data = input().splitlines()
    n, m = map(int, data[0].split())
    graph = []

    for i in range(1, m + 1):
        u, v, w = map(int, data[i].split())
        graph.append((u, v, w))

    result = floyd_warshall(n, graph)

    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()