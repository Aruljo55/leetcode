class Solution:
    def longestPalindrome(self, s):
        # Helper function to expand around the center
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left + 1:right]
        
        # If the string is empty or only one character, return the string itself
        if len(s) < 2:
            return s
        
        # Initialize variable to store the longest palindrome
        longest = ""
        
        # Loop through each character in the string
        for i in range(len(s)):
            # Find the longest palindrome with center at s[i] (odd-length palindromes)
            palindrome1 = expandAroundCenter(i, i)
            # Find the longest palindrome with center between s[i] and s[i+1] (even-length palindromes)
            palindrome2 = expandAroundCenter(i, i + 1)
            
            # Update the longest palindrome if a longer one is found
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest
