class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        # Initialize variables for the two transactions
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0

        for price in prices:
            # For the first transaction
            buy1 = max(buy1, -price)         # Maximize buying low
            sell1 = max(sell1, buy1 + price)  # Maximize selling high

            # For the second transaction
            buy2 = max(buy2, sell1 - price)  # Maximize buying after selling the first
            sell2 = max(sell2, buy2 + price)  # Maximize selling high in the second transaction

        return sell2
