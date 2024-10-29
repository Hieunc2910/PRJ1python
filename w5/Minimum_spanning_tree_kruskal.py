# Given a undirected connected graph G=(V,E) where V={1,…,N}. Each edge (u,v)∈E(u,v)∈E has weight w(u,v)w(u,v). Compute minimum spanning tree of G.
# Input
# Line 1: N and M (1≤N,M≤10
# 5
# ) in which NN is the number of nodes and MM is the number of edges.
# Line i+1 (i=1,…,M): contains 3 positive integers u, v, and w where w is the weight of edge (u,v)
# Output
# Write the weight of the minimum spanning tree found.
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_weight = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
    return mst_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    edges = []
    for i in range(1, m + 1):
        u, v, w = map(int, data[i].split())
        edges.append((u - 1, v - 1, w))  # Convert to 0-based index

    result = kruskal(n, edges)
    print(result)

if __name__ == "__main__":
    main()