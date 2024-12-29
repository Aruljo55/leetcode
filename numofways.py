class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)
        
        # Precompute character counts at each position
        count = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                count[i][ord(char) - ord('a')] += 1
        
        # Initialize dp array
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to form an empty target
        
        # Update dp array column by column
        for i in range(m):
            # Traverse target in reverse to avoid overwriting dp[j]
            for j in range(n - 1, -1, -1):
                char_idx = ord(target[j]) - ord('a')
                dp[j + 1] += dp[j] * count[i][char_idx]
                dp[j + 1] %= MOD
        
        return dp[n]
