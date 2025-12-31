class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False

# Examples
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False