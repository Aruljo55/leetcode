class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist
        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp

        # Reconnect the reversed sublist to the rest of the list
        prev.next.next = curr
        prev.next = next_node

        return dummy.next
