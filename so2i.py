class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        # If a is negative in 32-bit, convert it to Python's negative integer
        return a if a <= MAX else ~(a ^ MASK)
