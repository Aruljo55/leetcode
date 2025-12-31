from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Step 1: Sort by width asc, height desc
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Extract the heights
        heights = [h for w, h in envelopes]

        # Step 3: Apply LIS on heights
        dp = []
        for h in heights:
            idx = bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)
