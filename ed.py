from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # Build the graph
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0
            if src == dest:
                return 1.0
            visited.add(src)
            
            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    res = dfs(neighbor, dest, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0
        
        results = []
        for src, dest in queries:
            results.append(dfs(src, dest, set()))
        
        return results
