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

    def isUgly(self, n):
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1