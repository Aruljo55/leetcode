class Solution:
    def reorderedPowerOf2(self, n):
        s = sorted(str(n))
        for i in range(31):
            if sorted(str(1 << i)) == s:
                return True
        return False
