class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize to infinity
        max_profit = 0  # Initialize maximum profit
        
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit

# Example usage
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(solution.maxProfit(prices1))  # Output: 5
print(solution.maxProfit(prices2))  # Output: 0
