class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        last_a, last_b, last_c = -1, -1, -1
        
        for i, char in enumerate(s):
            if char == 'a':
                last_a = i
            elif char == 'b':
                last_b = i
            elif char == 'c':
                last_c = i
            
            if last_a != -1 and last_b != -1 and last_c != -1:
                min_pos = min(last_a, last_b, last_c)
                count += (min_pos + 1)
        
        return count