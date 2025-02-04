class Solution:
    def maxAscendingSum(self, nums):
        max_sum = curr_sum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
        return max(max_sum, curr_sum)
