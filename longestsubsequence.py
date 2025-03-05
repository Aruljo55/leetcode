class Solution:
    def lenLongestFibSubseq(self, arr):
        s = set(arr)
        n = len(arr)
        max_len = 0
        index_map = {val: i for i, val in enumerate(arr)}
        dp = {}
        
        for k in range(n):
            for j in range(k):
                i_val = arr[k] - arr[j]
                if i_val < arr[j] and i_val in index_map:
                    i = index_map[i_val]
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[(j, k)])
        
        return max_len if max_len >= 3 else 0
