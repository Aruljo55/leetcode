class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Append the integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        # If no remainder, return the result
        if remainder == 0:
            return "".join(result)
        
        # Append the decimal point
        result.append(".")
        
        # Dictionary to store the position of each remainder
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder is already seen, there's a repeating part
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            # Store the position of this remainder
            remainder_map[remainder] = len(result)
            
            # Multiply remainder by 10 and find the next digit
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)
