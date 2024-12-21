class Solution:
    def divide(self, dividend, divisor):
        # Handle the edge case of overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # If the result overflows, return the maximum value
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Subtract divisor from dividend until dividend is smaller than divisor
        while dividend >= divisor:
            current_divisor, num_divisors = divisor, 1
            # Double the divisor and count as long as it fits within the dividend
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                num_divisors <<= 1

            # Subtract the largest multiple found from the dividend
            dividend -= current_divisor
            quotient += num_divisors

        # Apply the sign
        if negative:
            quotient = -quotient

        # Ensure the result fits within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
