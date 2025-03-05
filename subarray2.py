class Solution:
    def maxAbsoluteSum(self, nums):
        max_sum = min_sum = 0
        curr_max = curr_min = 0
        
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, abs(min_sum))

# Example usage:
sol = Solution()
nums1 = [1,-3,2,3,-4]
nums2 = [2,-5,1,-4,3,-2]
print(sol.maxAbsoluteSum(nums1))  # Output: 5
print(sol.maxAbsoluteSum(nums2))  # Output: 8