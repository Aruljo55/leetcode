class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the built-in find method to find the first occurrence of needle in haystack
        return haystack.find(needle)

# Example usage:
solution = Solution()

# Test case 1: "sad" occurs at index 0
haystack1 = "sadbutsad"
needle1 = "sad"
print(solution.strStr(haystack1, needle1))  # Expected output: 0

# Test case 2: "leeto" does not occur in "leetcode"
haystack2 = "leetcode"
needle2 = "leeto"
print(solution.strStr(haystack2, needle2))  # Expected output: -1
     