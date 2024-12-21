class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy

        # Traverse both lists, adding the smaller node each time
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach any remaining elements
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next

