class Solution:
    def minPathSum(self, grid):
        # Get the number of rows (m) and columns (n)
        m, n = len(grid), len(grid[0])
        
        # Initialize the DP table with the same size as the grid
        dp = [[0] * n for _ in range(m)]
        
        # Base case: The top-left corner
        dp[0][0] = grid[0][0]
        
        # Fill in the first row (can only come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill in the first column (can only come from above)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill in the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right corner contains the result
        return dp[m-1][n-1]

