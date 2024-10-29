# Given a undirected graph =(V,E) in which V = {1,2,..,n} is the set of nodes. Write a program that visit nodes of G by a DFS (consider a lexicorgraphic order of nodes).
# Input
# Line 1: contains 2 integers n and m (1 <= n,m <= 100000)
# Line i+1: contains u and v which are two end-points of the ith edge
#
# Output
# Sequence of nodes visited by DFS
def dfs(graph, start, visited, result):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)

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
            dfs(graph, node, visited, result)

    print(" ".join(map(str, result)))

    if __name__ == "__main__":
        main()
