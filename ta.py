class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # 1) strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False

        # 2) strictly decreasing
        start = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == start:
            return False

        # 3) strictly increasing
        start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == start:
            return False

        return i == n - 1
