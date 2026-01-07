class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        total = 0

        # If left child exists and is a leaf
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # Recur on left and right subtrees
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total
