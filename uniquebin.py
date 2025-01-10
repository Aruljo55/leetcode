class Solution:
    def numTrees(self, n):
        # Dynamic programming approach
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one empty tree

        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1  # Nodes in the left subtree
                right = nodes - root  # Nodes in the right subtree
                dp[nodes] += dp[left] * dp[right]

        return dp[n]

# Example usage
solution = Solution()
n = 3
output = solution.numTrees(n)
print(output)
