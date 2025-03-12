import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the first half (lower half)
        self.small = []  # Max heap implemented as a min heap with negative values
        # Min heap for the second half (upper half)
        self.large = []  # Min heap
        
    def addNum(self, num: int) -> None:
        # By default, we'll add to the max heap (small numbers)
        heapq.heappush(self.small, -num)
        
        # Make sure every element in small is <= every element in large
        # Move the largest element from small to large if needed
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance the heaps
        # Ensure that the sizes of the heaps differ by at most 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        # If the sizes are equal, take the average of the two middle values
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        # Otherwise, take the middle value from the larger heap
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]