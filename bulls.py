from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_count = []
        guess_count = []
        
        # First pass: count bulls and collect non-bull characters
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count.append(s)
                guess_count.append(g)
        
        # Count frequency of remaining unmatched characters
        secret_freq = Counter(secret_count)
        guess_freq = Counter(guess_count)
        
        # Cows = sum of minimum count matches in both
        cows = sum(min(secret_freq[ch], guess_freq[ch]) for ch in secret_freq)
        
        return f"{bulls}A{cows}B"
