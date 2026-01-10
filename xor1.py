class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0

        for bit in range(31, -1, -1):
            mask |= (1 << bit)
            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            candidate = max_xor | (1 << bit)

            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    max_xor = candidate
                    break

        return max_xor
