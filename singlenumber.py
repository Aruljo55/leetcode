class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        diff = xor & -xor
        result = [0, 0]
        for num in nums:
            if num & diff == 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
