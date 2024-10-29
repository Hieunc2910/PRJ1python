# Given an undirected graph G = (V,E). Write a program to check if G is a Hamiltonian graph.
# Input
# Line 1: a positive integer T (number of graphs)
# Subsequent lines are information about T graphs, each has the following format:
# Line 1: n and m (number of nodes and edges)
# Line i+1 (i = 1, 2, ..., m): u and v : two end points of the ith edge
# Output
# In the ith line, write 1 if the corresponding is a Hamiltonian graph, and write 0, otherwise
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {i: [] for i in range(1, n + 1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_hamiltonian_util(self, path, pos):
        if pos == self.n:
            return path[0] in self.graph[path[pos - 1]]

        for v in range(1, self.n + 1):
            if v not in path and v in self.graph[path[pos - 1]]:
                path[pos] = v
                if self.is_hamiltonian_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def is_hamiltonian(self):
        path = [-1] * self.n
        path[0] = 1
        if not self.is_hamiltonian_util(path, 1):
            return 0
        return 1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        n, m = map(int, data[index].split())
        graph = Graph(n)
        index += 1
        for _ in range(m):
            u, v = map(int, data[index].split())
            graph.add_edge(u, v)
            index += 1
        results.append(graph.is_hamiltonian())

    for result in results:
        print(result)

if __name__ == "__main__":
    main()