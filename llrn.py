import random

class Solution:

    def __init__(self, head):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes)
