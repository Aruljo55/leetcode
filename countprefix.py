class Solution:
    def prefixCount(self, words, pref):
        return sum(1 for word in words if word.startswith(pref))
