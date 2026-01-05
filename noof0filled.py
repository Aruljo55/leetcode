class Solution:
    def zeroFilledSubarray(self, nums):
        cnt = 0
        cur = 0
        for x in nums:
            if x == 0:
                cur += 1
                cnt += cur
            else:
                cur = 0
        return cnt
