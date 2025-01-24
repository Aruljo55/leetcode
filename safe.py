from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        out_degree = [0] * n

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
            out_degree[node] = len(neighbors)

        queue = deque([node for node in range(n) if out_degree[node] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)
