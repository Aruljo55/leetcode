from collections import deque

class Solution:
    def magnificentSets(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        colors = {}
        
        def is_bipartite(node, color):
            queue = deque([(node, color)])
            while queue:
                curr, c = queue.popleft()
                if curr in colors:
                    if colors[curr] != c:
                        return False
                    continue
                colors[curr] = c
                for neighbor in graph[curr]:
                    queue.append((neighbor, 1 - c))
            return True
        
        def bfs_max_depth(start):
            queue = deque([start])
            visited = {start: 1}
            max_depth = 1
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited[neighbor] = visited[node] + 1
                        max_depth = max(max_depth, visited[neighbor])
                        queue.append(neighbor)
            return max_depth
        
        visited = set()
        result = 0
        for node in range(1, n + 1):
            if node not in visited:
                component = []
                queue = deque([node])
                while queue:
                    curr = queue.popleft()
                    if curr not in visited:
                        visited.add(curr)
                        component.append(curr)
                        queue.extend(graph[curr])
                
                if not is_bipartite(node, 0):
                    return -1
                
                max_group = 0
                for v in component:
                    max_group = max(max_group, bfs_max_depth(v))
                result += max_group
        return result
