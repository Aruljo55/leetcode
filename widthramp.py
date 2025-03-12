class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        max_width = 0
        
        # Step 1: Build a decreasing stack with indices
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Step 2: Traverse from right to left and calculate max width
        for j in reversed(range(len(nums))):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width
