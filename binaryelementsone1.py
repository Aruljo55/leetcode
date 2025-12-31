class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        min_ops = float('inf')
        
        for i in range(8):
            curr = nums.copy()
            ops = 0
            
            for j in range(3):
                if (i >> j) & 1:
                    if j + 2 < n:
                        curr[j] ^= 1
                        curr[j+1] ^= 1
                        curr[j+2] ^= 1
                        ops += 1
            
            for j in range(n - 2):
                if curr[j] == 0:
                    curr[j] ^= 1
                    curr[j+1] ^= 1
                    curr[j+2] ^= 1
                    ops += 1
            
            if curr[n-2] == 1 and curr[n-1] == 1:
                min_ops = min(min_ops, ops)
        
        return min_ops if min_ops != float('inf') else -1