class Solution:
    def countPrefixSuffixPairs(self, words):
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count

# Example usage:
solution = Solution()
words1 = ["a", "aba", "ababa", "aa"]
words2 = ["pa", "papa", "ma", "mama"]
words3 = ["abab", "ab"]

print(solution.countPrefixSuffixPairs(words1))  # Output: 4
print(solution.countPrefixSuffixPairs(words2))  # Output: 2
print(solution.countPrefixSuffixPairs(words3))  # Output: 0