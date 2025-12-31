class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

        # Fill the dp table
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = str2[:j]
                elif j == 0:
                    dp[i][j] = str1[:i]
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j] + str1[i - 1]) < len(dp[i][j - 1] + str2[j - 1]):
                        dp[i][j] = dp[i - 1][j] + str1[i - 1]
                    else:
                        dp[i][j] = dp[i][j - 1] + str2[j - 1]
        
        return dp[m][n]

# Example Usage
# sol = Solution()
# print(sol.shortestCommonSupersequence("abac", "cab"))