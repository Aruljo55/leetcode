class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clones = {}

        def dfs(original):
            if original.val in clones:
                return clones[original.val]

            copy = Node(original.val)
            clones[original.val] = copy

            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
