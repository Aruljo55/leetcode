class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        operations = 0

        curr_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] <= curr_sum:
                # must merge nums[i] with right part
                curr_sum += nums[i]
                operations += 1
            else:
                # no merge needed, reset
                curr_sum = nums[i]

        return operations
