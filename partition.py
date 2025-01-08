class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def partition(self, head, x):
        if not head:
            return None

        less_head = less_tail = self.ListNode(0)
        greater_head = greater_tail = self.ListNode(0)

        current = head

        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next

        # Combine the two partitions
        greater_tail.next = None
        less_tail.next = greater_head.next

        return less_head.next

# Example usage:
solution = Solution()

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = solution.ListNode(0)
    current = dummy
    for val in values:
        current.next = solution.ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head1 = create_linked_list([1, 4, 3, 2, 5, 2])
head2 = create_linked_list([2, 1])

x1 = 3
x2 = 2

result1 = solution.partition(head1, x1)
result2 = solution.partition(head2, x2)

print(linked_list_to_list(result1))  # Output: [1, 2, 2, 4, 3, 5]
print(linked_list_to_list(result2))  # Output: [1, 2]
