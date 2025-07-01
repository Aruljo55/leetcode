class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if freq[ch] < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))

        return len(s)
