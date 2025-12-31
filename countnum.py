class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        available = 9
        curr = 9
        for i in range(2, n + 1):
            curr *= available
            res += curr
            available -= 1
        return res
