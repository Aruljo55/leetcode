class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        left, right = 0, 0
        
        while left < len(words1) and words1[left] == words2[left]:
            left += 1
        
        while right < len(words1) and words1[-(right+1)] == words2[-(right+1)]:
            right += 1
        
        return left + right >= len(words1)
