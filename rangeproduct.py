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

        pref = [0]
        for p in powers:
            pref.append(pref[-1] + (p.bit_length() - 1))

        ans = []
        for l, r in queries:
            e = pref[r + 1] - pref[l]
            ans.append(pow(2, e, MOD))
        return ans
