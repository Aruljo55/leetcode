class Solution:
    def reorderedPowerOf2(self, n):
        target = sorted(str(n))
        for i in range(31):
            if sorted(str(1 << i)) == target:
                return True
        return False
