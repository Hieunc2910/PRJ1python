# Given undirected graph G = (V,E) in which V = {1, 2, ..., n} is the set of nodes, and E is the set of m edges.
# Write a program that computes the sequence of nodes visited using a BFS algorithm (the nodes are considered in a lexicographic order)
#
# Input
# Line 1: contains 2 integers n and m which are the number of nodes and the number of edges
# Line i+1 (i = 1, ..., m): contains 2 positive integers u and v which are the end points of the ith edge
#
# Output
# Write the sequence of nodes visited by a BFS procedure (nodes a are separated by a SPACE character)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    queue.append(neighbor)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    graph = {i: [] for i in range(1, n + 1)}

    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)

    visited = {i: False for i in range(1, n + 1)}
    result = []

    for node in range(1, n + 1):
        if not visited[node]:
            result.extend(bfs(graph, node, visited))

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()