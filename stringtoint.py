class Solution:
    def myAtoi(self, s):
        # Initialize index, sign, and result
        i = 0
        sign = 1
        result = 0
        length = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < length and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        if i < length and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Convert the digits
        while i < length and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before it happens
            if result > (2**31 - 1 - digit) // 10:
                return (2**31 - 1) if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        # Step 4: Apply the sign
        result *= sign
        
        # Step 5: Return the result
        return result
