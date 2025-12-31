class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] represents the minimum cost to guess the number between i and j
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # We start from the smallest subproblem where the range length is 2
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    # Cost of guessing at position k
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
        
        return dp[1][n]
