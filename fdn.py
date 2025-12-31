class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self._next

    def next(self):
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        return self._next is not None

class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
