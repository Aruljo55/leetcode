class Solution:
    def countPalindromicSubsequence(self, s):
        n = len(s)
        prefix_count = [[0] * n for _ in range(26)]
        suffix_count = [[0] * n for _ in range(26)]

        # Build prefix counts
        for i in range(n):
            if i > 0:
                for j in range(26):
                    prefix_count[j][i] = prefix_count[j][i - 1]
            prefix_count[ord(s[i]) - ord('a')][i] += 1

        # Build suffix counts
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                for j in range(26):
                    suffix_count[j][i] = suffix_count[j][i + 1]
            suffix_count[ord(s[i]) - ord('a')][i] += 1

        # Count unique palindromes
        unique_palindromes = set()
        for i in range(1, n - 1):
            middle_index = ord(s[i]) - ord('a')
            for left_char in range(26):
                if prefix_count[left_char][i - 1] > 0 and suffix_count[left_char][i + 1] > 0:
                    unique_palindromes.add((left_char, middle_index))

        return len(unique_palindromes)
