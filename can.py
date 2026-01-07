class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        # Handle negative numbers using 32-bit two's complement
        if num < 0:
            num = num + (1 << 32)

        hex_chars = "0123456789abcdef"
        result = ""

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num = num // 16

        return result
