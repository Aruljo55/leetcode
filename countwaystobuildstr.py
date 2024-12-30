class Solution:
    def countGoodStrings(self, low, high, zero, one):
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: there's one way to construct an empty string

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD  # Take modulo at every step to avoid overflow

        # Sum up the results for lengths in the range [low, high]
        return sum(dp[low:high + 1]) % MOD
