# Given a directed graph G = (V,E) in which V = {1,2,...,n) is the set of nodes. Each arc (u,v) has a non-negative weight w(u,v). Given two nodes s and t of G. Find the shortest path from s to t on G.
# Input
# Line 1: contains two integers n and m which are the number of nodes and the number of arcs of G (1 <= n <= 100000)
# Line i + 1(i = 1,2,...,m): contains 3 integers u, v, w in which w is the weight of arc(u,v) (0 <= w <= 100000)
# Line m+2: contains two integers s and t
# Output
# Write the weight of the shortest path found or write -1 if no path from s to t was found
#PYTHON
import heapq
import sys
input = sys.stdin.read
def dijkstra(n, graph, start, end):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end] if distances[end] != float('inf') else -1

def main():
    data = input().splitlines()
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n + 1)]

    for i in range(1, m + 1):
        u, v, w = map(int, data[i].split())
        graph[u].append((v, w))

    s, t = map(int, data[m + 1].split())

    result = dijkstra(n, graph, s, t)
    print(result)

if __name__ == "__main__":
    main()