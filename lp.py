class Solution:
    def longestPalindrome(self, s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        length = 0
        odd_used = False

        for v in freq.values():
            length += (v // 2) * 2
            if v % 2 == 1:
                odd_used = True

        if odd_used:
            length += 1

        return length
