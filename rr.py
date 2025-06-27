import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.idx = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False

        remove_idx = self.idx[val].pop()
        last_val = self.nums[-1]

        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val
            self.idx[last_val].add(remove_idx)
            self.idx[last_val].discard(len(self.nums) - 1)

        self.nums.pop()
        if not self.idx[val]:
            del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
