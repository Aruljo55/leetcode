class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg = 0
        mn = 10**18
        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                ax = abs(x)
                total += ax
                if ax < mn:
                    mn = ax
        if neg % 2 == 0:
            return total
        return total - 2 * mn
