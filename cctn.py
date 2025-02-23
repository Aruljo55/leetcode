class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)

        if left_depth == right_depth:
            return (2 ** left_depth) + self.countNodes(root.right)
        else:
            return (2 ** right_depth) + self.countNodes(root.left)

    def get_depth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth
