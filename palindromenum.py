class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digit numbers are palindromes
        if x < 10:
            return True
        
        # Reverse the number
        original = x
        reversed_number = 0
        
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10
        
        # Compare the original number with the reversed number
        return original == reversed_number
