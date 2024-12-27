class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # Get the number of rows (m) and columns (n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize a DP table with zeros
        dp = [[0] * n for _ in range(m)]
        
        # If the starting position has no obstacle, set dp[0][0] to 1
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        # Fill in the first column (can only come from above)
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill in the first row (can only come from the left)
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The bottom-right corner contains the result
        return dp[m-1][n-1]
