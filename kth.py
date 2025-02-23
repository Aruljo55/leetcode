import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
        return heap[0]

# Examples
solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
