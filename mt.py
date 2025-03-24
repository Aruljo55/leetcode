from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Step 2: Initialize the leaves
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        
        # Step 3: Trim the leaves
        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
        
        # Step 4: Return the remaining nodes (they are the MHT roots)
        return list(leaves)

# Example Usage
solution = Solution()
print(solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))  # Output: [1]
print(solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))  # Output: [3, 4]
