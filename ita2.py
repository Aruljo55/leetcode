from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result
