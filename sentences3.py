class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        i, j = 0, 0
        while i < len(words1) and words1[i] == words2[i]:
            i += 1
        
        while j < len(words1) and words1[-(j+1)] == words2[-(j+1)]:
            j += 1
        
        return i + j >= len(words1)

solution = Solution()
print(solution.areSentencesSimilar("My name is Haley", "My Haley"))  # Output: True
print(solution.areSentencesSimilar("of", "A lot of words"))         # Output: False
print(solution.areSentencesSimilar("Eating right now", "Eating"))    # Output: True
