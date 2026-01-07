class Solution:
    def maxProduct(self, root):
        MOD = 1000000007
        self.total = 0
        self.best = 0

        def sumTree(node):
            if not node:
                return 0
            s = node.val + sumTree(node.left) + sumTree(node.right)
            self.total = s
            return s

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.best = max(self.best, s * (self.total - s))
            return s

        sumTree(root)
        dfs(root)
        return self.best % MOD
