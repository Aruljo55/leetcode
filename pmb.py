class Solution:
    def putMarbles(self, weights, k):
        n = len(weights)
        
        # If k is 1, the only option is to put all marbles into one bag.
        if k == 1:
            return (weights[0] + weights[-1]) * 2
        
        # Initialize arrays for the dp table
        dp_min = [float('inf')] * (n + 1)
        dp_max = [-float('inf')] * (n + 1)
        
        # Prefix sum array to calculate costs quickly
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + weights[i]
        
        # Base case: 0 marbles and 0 bags have score 0
        dp_min[0] = dp_max[0] = 0
        
        # Fill DP table
        for bags in range(1, k + 1):
            for i in range(bags, n + 1):  # We need at least 'bags' marbles
                for j in range(bags - 1, i):  # Iterate over possible splits
                    cost = weights[j] + weights[i - 1]
                    dp_min[i] = min(dp_min[i], dp_min[j] + cost)
                    dp_max[i] = max(dp_max[i], dp_max[j] + cost)
        
        # The final answer is the difference between the max and min scores
        return dp_max[n] - dp_min[n]
        
# Test case:
weights = [1, 3, 5, 1]
k = 2
print(Solution().putMarbles(weights, k))  # Expected output: 4
