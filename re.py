class Solution:
    def removeElement(self, nums, val):
        i = 0  # Pointer for the next valid position
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # Move non-val element forward
                i += 1  # Increment valid count
        return i  # Length of new valid elements

# Test cases
sol = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = sol.removeElement(nums1, val1)
print(k1, nums1[:k1])  # Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = sol.removeElement(nums2, val2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 3, 0, 4]
