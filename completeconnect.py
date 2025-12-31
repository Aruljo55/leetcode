class Solution:
    def countCompleteComponents(self, n, edges):
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            component = []
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            stack.append(v)
            return component
        
        def is_complete(component):
            k = len(component)
            required_edges = k * (k - 1) // 2
            edge_count = 0
            for i in range(k):
                for j in range(i + 1, k):
                    if component[j] in adj[component[i]]:
                        edge_count += 1
            return edge_count == required_edges
        
        complete_components_count = 0
        
        for i in range(n):
            if not visited[i]:
                component = dfs(i)
                if is_complete(component):
                    complete_components_count += 1
        
        return complete_components_count
