class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True
        remaining = n

        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left = not left

        return head
