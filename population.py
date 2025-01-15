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
        
        # Start with the leftmost node of the current level
        leftmost = root
        
        while leftmost.left:  # As long as there are levels to process
            # Traverse nodes in the current level
            current = leftmost
            while current:
                # Connect left and right children of the current node
                current.left.next = current.right
                
                # Connect right child to the next node's left child if available
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root
