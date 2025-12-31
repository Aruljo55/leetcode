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

    def checkPowersOfThree(self, n):
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

    def areSentencesSimilar(self, sentence1, sentence2):
        words1, words2 = sentence1.split(), sentence2.split()
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        while words2 and words1[0] == words2[0]:
            words1.pop(0)
            words2.pop(0)
        while words2 and words1[-1] == words2[-1]:
            words1.pop()
            words2.pop()
        return not words2

    def minLength(self, s):
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 2 and (stack[-2] + stack[-1] == "AB" or stack[-2] + stack[-1] == "CD"):
                stack.pop()
                stack.pop()
        return len(stack)
