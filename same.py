class Solution:
    def isSameTree(self, p, q):
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one is None or values differ, they are not the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
