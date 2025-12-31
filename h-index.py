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

    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5
        for _ in range(1, n):
            nextUgly = min(next2, next3, next5)
            ugly.append(nextUgly)
            if nextUgly == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if nextUgly == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if nextUgly == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]

    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return below_20[num // 100] + " Hundred " + helper(num % 100)

        result = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()

    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break
        return h