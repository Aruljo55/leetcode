from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        mid = ''
        left_half = []

        for ch in sorted(count):  # sort ensures lexicographical order
            if count[ch] % 2 == 1:
                if mid:
                    # Should never happen due to the problem constraints
                    return ""
                mid = ch
            left_half.append(ch * (count[ch] // 2))
        
        left = ''.join(left_half)
        return left + mid + left[::-1]
