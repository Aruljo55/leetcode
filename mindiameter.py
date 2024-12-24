from collections import deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def tree_diameter(edges, n):
            def bfs(node):
                dist = [-1] * n
                dist[node] = 0
                q = deque([node])
                farthest_node = node
                while q:
                    curr = q.popleft()
                    for neighbor in adj[curr]:
                        if dist[neighbor] == -1:
                            dist[neighbor] = dist[curr] + 1
                            q.append(neighbor)
                            farthest_node = neighbor
                return farthest_node, dist[farthest_node]

            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            farthest_node, _ = bfs(0)
            _, diameter = bfs(farthest_node)
            return diameter

        n = len(edges1) + 1
        m = len(edges2) + 1
        d1 = tree_diameter(edges1, n)
        d2 = tree_diameter(edges2, m)
        return max(d1, d2) + 1
