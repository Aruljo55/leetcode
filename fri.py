from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        result = [-1] * n
        
        # Keep start values with original indices
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        for i, (start, end) in enumerate(intervals):
            # Binary search to find the minimal start >= end
            idx = bisect_left(starts, (end,))  # (end,) because starts is list of tuples
            if idx < n:
                result[i] = starts[idx][1]
        
        return result
