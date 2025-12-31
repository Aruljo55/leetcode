from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        freq = defaultdict(int)
        left = 0
        count_pairs = 0
        res = 0
        
        for right in range(len(nums)):
            # Add nums[right] to the window
            count_pairs += freq[nums[right]]
            freq[nums[right]] += 1
            
            # Shrink from left while we have enough pairs
            while count_pairs >= k:
                res += len(nums) - right
                freq[nums[left]] -= 1
                count_pairs -= freq[nums[left]]
                left += 1

        return res
