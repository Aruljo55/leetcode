class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
