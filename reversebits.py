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
    
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
    
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
