import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  # Start point (negative for max heap)
            points.append((right, height))  # End point

        points.sort(key=lambda x: (x[0], x[1]))
        result = []
        heap = [0]
        prev_height = 0

        for x, h in points:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapq.heapify(heap)

            current_height = -heap[0]
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result

# Examples
solution = Solution()
print(solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
# Output: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

print(solution.getSkyline([[0, 2, 3], [2, 5, 3]]))
# Output: [[0, 3], [5, 0]]
