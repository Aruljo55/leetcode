from collections import Counter

class Solution:
    def canConstruct(self, s, k):
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # Check the conditions
        if k > len(s):
            return False
        if k < odd_count:
            return False
        return True
