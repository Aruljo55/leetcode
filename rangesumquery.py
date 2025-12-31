class NumArray:

    def __init__(self, nums):
        # Initialize the prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)  # One extra for base case
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        # Use the prefix sum array to get the sum of the subarray [left, right]
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
