class Solution:
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 1: Precompute if each word starts and ends with a vowel
        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        
        # Step 2: Compute the prefix sum
        n = len(words)
        prefix = [0] * n
        prefix[0] = is_vowel_word[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + is_vowel_word[i]
        
        # Step 3: Answer each query
        ans = []
        for li, ri in queries:
            if li == 0:
                ans.append(prefix[ri])
            else:
                ans.append(prefix[ri] - prefix[li - 1])
        
        return ans
