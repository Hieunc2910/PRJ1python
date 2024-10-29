# given a network G = (V, E) which is a directed weighted graph. Node s is the source and node t is the target. c(u,v) is the capacity of the arc (u,v). Find the maximum flow on G.
# Input
# •Line 1: two positive integers N and M (1 <= N <= 10^4, 1 <= M <= 10^6)
# •Line 2: contains 2 positive integers s and t
# •Line i+2 (I = 1,. . ., M): contains two positive integers u and v which are endpoints of ith arc
# Output
#   Write the value of the max-flow found
from collections import deque, defaultdict


def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False


def edmonds_karp(n, capacity, source, sink):
    parent = {}
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    s, t = map(int, data[1].split())

    capacity = defaultdict(lambda: defaultdict(int))

    for i in range(2, 2 + m):
        u, v, c = map(int, data[i].split())
        capacity[u][v] += c

    result = edmonds_karp(n, capacity, s, t)
    print(result)


if __name__ == "__main__":
    main()