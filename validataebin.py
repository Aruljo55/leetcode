class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def isValidBSTHelper(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return (isValidBSTHelper(node.left, lower, node.val) and
                    isValidBSTHelper(node.right, node.val, upper))
        
        return isValidBSTHelper(root, float('-inf'), float('inf'))
