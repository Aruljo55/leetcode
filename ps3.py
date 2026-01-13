from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        prefix = defaultdict(int)
        prefix[0] = 1  # Base case
        self.count = 0

        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
            # If a previous prefix sum exists, it forms a valid path
            self.count += prefix[current_sum - targetSum]
            
            prefix[current_sum] += 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            prefix[current_sum] -= 1  # Backtrack
        
        dfs(root, 0)
        return self.count
