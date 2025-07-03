class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        
        # Group consecutive characters
        groups = []
        prev = word[0]
        count = 1
        for c in word[1:]:
            if c == prev:
                count += 1
            else:
                groups.append(count)
                prev = c
                count = 1
        groups.append(count)
        
        total_length = sum(groups)
        answer = 0
        
        # Original word itself
        if total_length >= k:
            answer += 1
        
        # Try removing any number from any single group
        for g in groups:
            for remove in range(1, g):
                if total_length - remove >= k:
                    answer += 1
        
        return answer % MOD
