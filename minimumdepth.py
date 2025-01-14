# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0  # Base case: An empty tree has a depth of 0
        
        # If one of the subtrees is None, consider the depth of the other subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both subtrees are present, take the minimum of the two depths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
