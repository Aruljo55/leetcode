class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        rounds = minutesToTest // minutesToDie
        pigs = 0

        while (rounds + 1) ** pigs < buckets:
            pigs += 1

        return pigs
