class Solution:
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        operations = 0

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0

            # find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # merge the pair
            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)

            operations += 1

        return operations
