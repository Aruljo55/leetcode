class Solution:
    def coinChange(self, coins, amount):
        # Initialize DP array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case: 0 coins to make amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
