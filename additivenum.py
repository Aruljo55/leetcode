class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # Try every possible split of the first two numbers
        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]
                
                # Skip numbers with leading zeros, except "0" itself
                if (num1[0] == '0' and num1 != '0') or (num2[0] == '0' and num2 != '0'):
                    continue
                
                # Now check if the rest of the string follows the additive property
                while j < n:
                    num3 = str(int(num1) + int(num2))  # The next number should be the sum of num1 and num2
                    if not num.startswith(num3, j):  # Check if the next part of the string matches num3
                        break
                    j += len(num3)
                    num1, num2 = num2, num3  # Update num1 and num2 to be the last two numbers
                
                    # If we reached the end of the string, it's a valid sequence
                    if j == n:
                        return True

        return False
