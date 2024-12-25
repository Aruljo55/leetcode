class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # If the merged list is empty or there is no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
