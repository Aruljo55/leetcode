class Solution:
    def sortColors(self, nums):
        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse the array
        while mid <= high:
            if nums[mid] == 0:  # Red
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # White
                mid += 1
            else:  # Blue
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
