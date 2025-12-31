class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            val = matrix[i][j]
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > val:
                    dp[i][j] = max(dp[i][j], dfs(ni, nj))
            dp[i][j] += 1
            return dp[i][j]

        return max(dfs(i, j) for i in range(m) for j in range(n))
