class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # Convert to list to modify
        left, right = 0, len(s) - 1

        while left < right:
            # Move left to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
