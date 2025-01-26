class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element, 
            # then the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than or equal to the rightmost element, 
            # then the minimum is in the left half (including mid)
            elif nums[mid] < nums[right]:
                right = mid
            # If the middle element is equal to the rightmost element, we can't decide, 
            # so we reduce the search space by incrementing the right pointer
            else:
                right -= 1
        
        return nums[left]
