class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        size = 1
        while size < n:
            size *= 2
        seg = [0] * (2 * size)
        for i in range(n):
            seg[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        def find_leftmost(val):
            if seg[1] < val:
                return -1
            i = 1
            while i < size:
                if seg[2 * i] >= val:
                    i = 2 * i
                else:
                    i = 2 * i + 1
            return i - size

        def update(idx):
            i = idx + size
            seg[i] = 0
            i //= 2
            while i:
                seg[i] = max(seg[2 * i], seg[2 * i + 1])
                i //= 2

        unplaced = 0
        for f in fruits:
            idx = find_leftmost(f)
            if idx == -1:
                unplaced += 1
            else:
                update(idx)
        return unplaced
