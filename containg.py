class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        def contains_all_vowels(vowel_count):
            return all(vowel_count.get(v, 0) > 0 for v in vowels)
        
        n = len(word)
        result = 0
        
        for start in range(n):
            vowel_count = {}
            consonant_count = 0
            
            for end in range(start, n):
                char = word[end]
                
                if char in vowels:
                    vowel_count[char] = vowel_count.get(char, 0) + 1
                else:
                    consonant_count += 1
                
                if consonant_count == k and contains_all_vowels(vowel_count):
                    result += 1
                
                if consonant_count > k:
                    break
        
        return result