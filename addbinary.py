class Solution:
    def addBinary(self, a, b):
        # Initialize pointers for both strings
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Iterate over both strings
        while i >= 0 or j >= 0 or carry:
            # Add the current bits from both strings, if they exist
            sum_val = carry
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
            
            # The current bit is sum_val % 2
            result.append(str(sum_val % 2))
            
            # Update carry for the next position
            carry = sum_val // 2
        
        # Reverse the result list and return as a string
        return ''.join(result[::-1])

# Example usage for testing
solution = Solution()
print(solution.addBinary("11", "1"))  # Output: "100"
print(solution.addBinary("1010", "1011"))  # Output: "10101"
