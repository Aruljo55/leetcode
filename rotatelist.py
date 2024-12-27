class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Compute the length of the list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Connect the tail to the head to form a circle
        current.next = head
        
        # Find the new tail: (length - k % length - 1)th node
        # Find the new head: (length - k % length)th node
        k = k % length
        steps_to_new_tail = length - k - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None  # Break the circle
        
        return new_head

# Helper functions to test the solution
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
solution = Solution()
head = list_to_linked_list([1, 2, 3, 4, 5])
rotated = solution.rotateRight(head, 2)
print(linked_list_to_list(rotated))  # Output: [4, 5, 1, 2, 3]

head = list_to_linked_list([0, 1, 2])
rotated = solution.rotateRight(head, 4)
print(linked_list_to_list(rotated))  # Output: [2, 0, 1]
