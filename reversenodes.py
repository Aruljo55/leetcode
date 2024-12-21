class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to reverse a portion of the linked list
        def reverse_linked_list(start, end):
            prev, current = None, start
            while current != end:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev

        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Main loop to process each group of k nodes
        while True:
            # Check if there are at least k nodes remaining to reverse
            count = 0
            group_start = current.next
            temp = current
            while count < k and temp.next:
                temp = temp.next
                count += 1

            if count < k:
                break  # Less than k nodes remaining, so exit the loop

            # Reverse the k nodes
            group_end = temp.next
            new_start = reverse_linked_list(group_start, group_end)

            # Reconnect the reversed group with the rest of the list
            current.next = new_start
            group_start.next = group_end
            current = group_start

        return dummy.next
