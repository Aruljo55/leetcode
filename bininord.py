class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Visit left subtree
            result.append(node.val)  # Visit node
            inorder(node.right)  # Visit right subtree
        
        inorder(root)
        return result
