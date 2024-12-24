from itertools import permutations

class Solution:
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result

# Example Usage
nums1 = [1, 2, 3]
solution = Solution()
print(solution.permute(nums1))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums2 = [0, 1]
print(solution.permute(nums2))  # Output: [[0,1],[1,0]]

nums3 = [1]
print(solution.permute(nums3))  # Output: [[1]]
