class Solution:
    def productQueries(self, n, queries):
        MOD = 1000000007
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1

        prefix = [0]
        for x in powers:
            prefix.append(prefix[-1] + (x.bit_length() - 1))

        res = []
        for l, r in queries:
            exp = prefix[r + 1] - prefix[l]
            res.append(pow(2, exp, MOD))
        return res
