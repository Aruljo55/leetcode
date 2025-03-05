class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = [num for num in nums if num != 0] + [0] * nums.count(0)
        return result

# Example Usage
# sol = Solution()
# print(sol.applyOperations([1, 2, 2, 1, 1, 0]))  # Output: [1, 4, 2, 0, 0, 0]
