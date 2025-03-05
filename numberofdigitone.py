class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            left = n // (factor * 10)
            digit = (n // factor) % 10
            right = n % factor

            if digit > 1:
                count += (left + 1) * factor
            elif digit == 1:
                count += left * factor + right + 1
            else:
                count += left * factor

            factor *= 10
        return count