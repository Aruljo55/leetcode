class Solution:
    def isPalindrome(self, s):
        # Filter the string to include only alphanumeric characters and convert to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the filtered string is a palindrome
        return filtered == filtered[::-1]

# Example usage for testing:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(solution.isPalindrome("race a car"))                     # Output: False
    print(solution.isPalindrome(" "))                              # Output: True
