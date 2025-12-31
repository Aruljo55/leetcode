class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_part = ''.join('a' if c == 'z' else chr(ord(c) + 1) for c in word)
            word += next_part
        return word[k - 1]
