class Solution:
    def findParent(self, parent, node):
        if parent[node] != node:
            parent[node] = self.findParent(parent, parent[node])
        return parent[node]
    
    def union(self, parent, rank, u, v):
        rootU = self.findParent(parent, u)
        rootV = self.findParent(parent, v)
        
        if rootU == rootV:
            return False
        
        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        elif rank[rootU] < rank[rootV]:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU
            rank[rootU] += 1
        
        return True
    
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        for u, v in edges:
            if not self.union(parent, rank, u, v):
                return [u, v]
        
        return []
