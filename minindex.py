class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
        
        # Step 1: Find the dominant element
        dominant = max(set(nums), key=nums.count)
        
        # Step 2: Compute the prefix and suffix counts of the dominant element
        prefix_count = [0] * n
        suffix_count = [0] * n
        
        # Fill prefix_count
        prefix_count[0] = 1 if nums[0] == dominant else 0
        for i in range(1, n):
            prefix_count[i] = prefix_count[i - 1] + (1 if nums[i] == dominant else 0)
        
        # Fill suffix_count
        suffix_count[n - 1] = 1 if nums[n - 1] == dominant else 0
        for i in range(n - 2, -1, -1):
            suffix_count[i] = suffix_count[i + 1] + (1 if nums[i] == dominant else 0)
        
        # Step 3: Check for valid splits
        for i in range(n - 1):  # valid splits are at indices i, where 0 <= i < n - 1
            if prefix_count[i] * 2 > (i + 1) and suffix_count[i + 1] * 2 > (n - i - 1):
                return i
        
        return -1  # No valid split found
