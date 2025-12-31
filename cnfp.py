from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]
            # Search in the right side (i+1 to end)
            left_index = bisect_left(nums, low, i + 1, n)
            right_index = bisect_right(nums, high, i + 1, n)
            count += right_index - left_index

        return count
