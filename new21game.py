class Solution:
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                res += dp[i]
            if i - maxPts >= 0:
                window -= dp[i - maxPts]

        return res
