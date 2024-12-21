class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps forward
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next