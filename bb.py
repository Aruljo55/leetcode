class Solution:
    def maxCoins(self, nums):
        # Add virtual balloons at each end
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Fill the dp table
        for length in range(2, n):  # length is the subarray length
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )

        return dp[0][n - 1]
