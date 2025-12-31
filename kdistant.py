class Solution:
    def findKDistantIndices(self, nums, key, k):
        result = set()

        for i, num in enumerate(nums):
            if num == key:
                # Add all indices in the range [i - k, i + k]
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    result.add(j)

        return sorted(result)
