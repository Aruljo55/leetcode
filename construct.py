class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # Root is the first element of preorder
        root = TreeNode(preorder[0])
        
        # Find the root index in inorder traversal
        root_index = inorder.index(preorder[0])
        
        # Build left and right subtrees recursively
        root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])
        
        return root
