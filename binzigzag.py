from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # Direction flag
        
        while queue:
            level_size = len(queue)
            level_nodes = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Append to level_nodes based on direction
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append current level to result
            result.append(list(level_nodes))
            
            # Toggle direction
            left_to_right = not left_to_right
        
        return result
