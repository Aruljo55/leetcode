class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node to act as the previous node for the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Loop through the list while there are at least two nodes to swap
        while current.next and current.next.next:
            # Identify the two nodes to swap
            first = current.next
            second = current.next.next

            # Swapping the nodes
            first.next = second.next
            second.next = first
            current.next = second

            # Move the pointer to the next pair
            current = first
        
        # Return the new head of the list
        return dummy.next
