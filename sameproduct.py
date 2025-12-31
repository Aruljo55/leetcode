from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                prod_count[nums[i] * nums[j]] += 1
        res = 0
        for count in prod_count.values():
            if count > 1:
                res += count * (count - 1) * 4
        return res
