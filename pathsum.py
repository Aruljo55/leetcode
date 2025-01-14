# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False  # Base case: empty tree
        
        # Check if it's a leaf node and the targetSum matches the node's value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
