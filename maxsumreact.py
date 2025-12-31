from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')

        for top in range(m):
            # Initialize column sums
            col_sums = [0] * n
            for bottom in range(top, m):
                # Update column sums between top and bottom rows
                for col in range(n):
                    col_sums[col] += matrix[bottom][col]
                
                # Use TreeSet (SortedList) to find max subarray sum ≤ k
                prefix_sum = 0
                prefix_sums = SortedList([0])  # initialize with 0
                curr_max = float('-inf')
                
                for sum_ in col_sums:
                    prefix_sum += sum_
                    # We want smallest prefix ≥ prefix_sum - k
                    idx = prefix_sums.bisect_left(prefix_sum - k)
                    if idx < len(prefix_sums):
                        curr_max = max(curr_max, prefix_sum - prefix_sums[idx])
                    prefix_sums.add(prefix_sum)
                
                res = max(res, curr_max)
        
        return res
