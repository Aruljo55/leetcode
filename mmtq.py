class Solution:
    def minMoves(self, nums):
        m = min(nums)
        return sum(nums) - m * len(nums)
