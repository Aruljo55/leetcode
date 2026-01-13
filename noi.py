class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap → remove this interval
                removals += 1
            else:
                # No overlap → update prev_end
                prev_end = intervals[i][1]

        return removals
