class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1

        seg = [0] * (2 * size)

        for i in range(n):
            seg[size + i] = baskets[i]

        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        def update(pos, value):
            pos += size
            seg[pos] = value
            pos //= 2
            while pos:
                seg[pos] = max(seg[2 * pos], seg[2 * pos + 1])
                pos //= 2

        def query(val):
            if seg[1] < val:
                return -1
            idx = 1
            while idx < size:
                if seg[2 * idx] >= val:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - size

        unplaced = 0

        for fruit in fruits:
            idx = query(fruit)
            if idx == -1:
                unplaced += 1
            else:
                update(idx, 0)

        return unplaced
