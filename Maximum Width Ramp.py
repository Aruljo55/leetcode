class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        max_width = 0
        
        # Build a decreasing stack of indices
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        # Traverse from the end and calculate max width
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width

# Example Test Cases
solution = Solution()
print(solution.maxWidthRamp([6, 0, 8, 2, 1, 5]))  # Output: 4
print(solution.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))  # Output: 7
