class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)  # Convert wordDict to a set for faster lookup
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can be segmented

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
