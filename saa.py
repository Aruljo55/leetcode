import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> list[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> list[int]:
        shuffled = self.nums[:]
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
