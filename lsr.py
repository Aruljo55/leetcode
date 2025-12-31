from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Check if t * k is a subsequence of s
        def is_subsequence(t):
            t_repeated = t * k
            i = 0
            for c in s:
                if i == len(t_repeated):
                    break
                if c == t_repeated[i]:
                    i += 1
            return i == len(t_repeated)

        # DFS to explore possible subsequences
        def dfs(curr):
            nonlocal res
            if is_subsequence(curr):
                if len(curr) > len(res) or (len(curr) == len(res) and curr > res):
                    res = curr
            if len(curr) == max_len:
                return
            for c in sorted(chars, reverse=True):
                dfs(curr + c)

        # Count characters that appear at least k times
        counter = Counter(s)
        chars = [c for c in counter if counter[c] >= k]
        max_len = sum(counter[c] // k for c in counter)
        max_len = min(max_len, 7)  # pruning to reduce DFS depth

        res = ""
        dfs("")
        return res


# ✅ Example to run
s = "letsleetcode"
k = 2
sol = Solution()
print(sol.longestSubsequenceRepeatedK(s, k))  # Output: "let"
