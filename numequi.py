class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = {}
        result = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            result += count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        return result