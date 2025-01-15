class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None
        
        # Start with the root node
        current = root
        
        while current:
            # Dummy node to build the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level
            current = dummy.next
        
        return root
