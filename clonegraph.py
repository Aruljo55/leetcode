class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]
            
            copy = Node(current_node.val)
            visited[current_node] = copy
            
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)
