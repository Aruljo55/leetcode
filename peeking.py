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
