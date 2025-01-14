# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        # Helper function to check if the tree is balanced
        def check_height(node):
            if not node:
                return 0  # An empty subtree is balanced and has height 0
            
            # Recursively check the left and right subtrees
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree
            return max(left_height, right_height) + 1
        
        # Start the recursive check from the root
        return check_height(root) != -1
