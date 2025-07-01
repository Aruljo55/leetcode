class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        MOD = 10**9 + 7

        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % MOD

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return res
