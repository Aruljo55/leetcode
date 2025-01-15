class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: dp[i][0] = 1 for all i
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        # The answer is dp[m][n]
        return dp[m][n]
