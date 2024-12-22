class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse both numbers
        num1, num2 = num1[::-1], num2[::-1]
        n, m = len(num1), len(num2)
        
        # Result array to store the product
        result = [0] * (n + m)

        # Multiply each digit and add the result to the appropriate position
        for i in range(n):
            for j in range(m):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                # Carry handling
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert the result back to a string
        return ''.join(map(str, result[::-1]))

# Example usage
solution = Solution()
print(solution.multiply("2", "3"))         # Output: "6"
print(solution.multiply("123", "456"))     # Output: "56088"
