from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, value: int) -> None:
        if value not in self.nums:
            self.nums.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.nums:
            return []

        intervals = []
        start = end = self.nums[0]

        for num in self.nums[1:]:
            if num == end + 1:
                end = num
            else:
                intervals.append([start, end])
                start = end = num
        intervals.append([start, end])
        return intervals
