# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a BST to a single string."""
        res = []

        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to BST."""
        if not data:
            return None

        preorder = list(map(int, data.split(",")))
        idx = [0]   # mutable index

        def build(lower, upper):
            if idx[0] == len(preorder):
                return None

            val = preorder[idx[0]]
            if val < lower or val > upper:
                return None

            idx[0] += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float("-inf"), float("inf"))
