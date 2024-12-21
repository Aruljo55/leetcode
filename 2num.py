class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node to simplify the result list construction
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get the values from the current nodes of l1 and l2 (or 0 if the node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the two digits and the carry
            total = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = total // 10
            
            # Create a new node with the digit part of the total
            current.next = ListNode(total % 10)
            
            # Move the current pointer to the new node
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next node of dummy_head which is the head of the result list
        return dummy_head.next

# Helper function to print linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy_head = ListNode(0)
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Example usage:
l1_values = [2, 4, 3]  # Represents the number 342
l2_values = [5, 6, 4]  # Represents the number 465

# Create linked lists from values
l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

# Instantiate the Solution class and use the addTwoNumbers method
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result linked list: 7 -> 0 -> 8
print_linked_list(result)
