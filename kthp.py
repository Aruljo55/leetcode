import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []
        
        # Insert the first element of each row into the heap
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, column)
        
        # Extract the smallest element k times
        for _ in range(k - 1):
            val, row, col = heapq.heappop(min_heap)
            
            # If there is a next element in the same row, push it into the heap
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        
        # The kth smallest element is now at the top of the heap
        return heapq.heappop(min_heap)[0]
