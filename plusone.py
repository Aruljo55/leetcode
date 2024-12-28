class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):  # Traverse the array backward
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # If current digit is 9, set to 0 and carry over

        # If all digits were 9, we need to add an extra digit at the front
        return [1] + digits
