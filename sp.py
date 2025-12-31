class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        temp = s + '#' + s[::-1]
        lps = [0] * len(temp)

        for i in range(1, len(temp)):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j

        return s[lps[-1]:][::-1] + s

# Examples
solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(solution.shortestPalindrome("abcd"))      # Output: "dcbabcd"
