class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Edge case: empty list
        
        i = 0  # Pointer for the next unique position
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1  # Move unique pointer
                nums[i] = nums[j]  # Update position
        
        return i + 1  # Unique count (1-based index)

# Test cases
sol = Solution()

nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
