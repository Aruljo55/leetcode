from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        count_map = defaultdict(int)
        good_pairs = 0
        n = len(nums)
        
        for j in range(n):
            diff = nums[j] - j
            good_pairs += count_map[diff]
            count_map[diff] += 1
        
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs
