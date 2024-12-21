class Solution:
    def reverse(self, x):
        # Handle the sign of x
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            pop = x % 10  # Get the last digit
            x //= 10      # Remove the last digit from x
            
            # Check for overflow before appending the digit to reversed_x
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and pop > 7):
                return 0  # Overflow for positive numbers
            if reversed_x > (2**31) // 10 or (reversed_x == (2**31) // 10 and pop > 8):
                return 0  # Overflow for negative numbers

            reversed_x = reversed_x * 10 + pop  # Append the digit

        return sign * reversed_x

