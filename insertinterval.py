class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0

        # Add all intervals that come before the new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the new interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Add all remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
