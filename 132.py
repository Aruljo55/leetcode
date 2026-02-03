class Solution:
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')

        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True

            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            stack.append(nums[i])

        return False
