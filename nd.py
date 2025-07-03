class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1
        
        # Find the digit length group
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        
        # Find the number where the nth digit is
        number = start + (n - 1) // digits
        
        # Find the digit in the number
        digit_index = (n - 1) % digits
        return int(str(number)[digit_index])
