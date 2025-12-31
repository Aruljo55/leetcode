class Solution:
    def numSquares(self, n):
        # Create dp array initialized with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # List all perfect squares <= n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]
