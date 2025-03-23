class NumArray:
    def __init__(self, nums: list):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        
        # Building the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        # Update the value at index and propagate the changes
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        # Sum from index left to right
        left += self.n
        right += self.n
        total = 0
        
        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        
        return total
