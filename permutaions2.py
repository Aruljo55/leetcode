from itertools import permutations

class Solution:
    def permuteUnique(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        nums.sort()
        result = []
        backtrack(0)
        return result

# Example Usage
nums1 = [1, 1, 2]
solution = Solution()
print(solution.permuteUnique(nums1))  # Output: [[1,1,2],[1,2,1],[2,1,1]]

nums2 = [1, 2, 3]
print(solution.permuteUnique(nums2))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
