class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)  # 1-indexed

    def update(self, i, delta):
        i += 1  # make it 1-indexed
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1  # make it 1-indexed
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = {val: idx for idx, val in enumerate(nums2)}
        arr = [pos2[val] for val in nums1]

        left_tree = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_tree.query(arr[i] - 1)
            left_tree.update(arr[i], 1)

        right_tree = FenwickTree(n)
        right_larger = [0] * n
        for i in range(n - 1, -1, -1):
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(arr[i])
            right_tree.update(arr[i], 1)

        total = sum(l * r for l, r in zip(left_smaller, right_larger))
        return total
