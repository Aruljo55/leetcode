from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            subtree_sum = values[node]
            valid_splits = 0

            for neighbor in graph[node]:
                if neighbor != parent:
                    child_sum, child_splits = dfs(neighbor, node)
                    subtree_sum += child_sum
                    valid_splits += child_splits

            if subtree_sum % k == 0:
                valid_splits += 1
                return 0, valid_splits

            return subtree_sum, valid_splits

        _, result = dfs(0, -1)
        return result
