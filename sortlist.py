class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        # Create a dummy node to handle edge cases and simplify the logic
        dummy = ListNode(0)
        dummy.next = head
        current = head
        
        while current and current.next:
            if current.val <= current.next.val:
                # If the current node is in order, just move to the next node
                current = current.next
            else:
                # Find the correct position to insert current.next node
                prev = dummy
                while prev.next.val <= current.next.val:
                    prev = prev.next
                # Insert the node by adjusting the pointers
                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
        
        return dummy.next
