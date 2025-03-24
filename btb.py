class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # DP arrays
        hold = [0] * n
        sell = [0] * n
        cooldown = [0] * n
        
        # Base cases
        hold[0] = -prices[0]  # We buy the stock on day 0
        sell[0] = 0            # No profit if we sell on day 0
        cooldown[0] = 0        # No profit in cooldown state on day 0
        
        for i in range(1, n):
            # Recurrence relations
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            cooldown[i] = max(cooldown[i-1], sell[i-1])
        
        # The answer is the maximum of sell[n-1] and cooldown[n-1]
        return max(sell[n-1], cooldown[n-1])

# Example Usage:
solution = Solution()
prices1 = [1, 2, 3, 0, 2]
print(solution.maxProfit(prices1))  # Output: 3

prices2 = [1]
print(solution.maxProfit(prices2))  # Output: 0
