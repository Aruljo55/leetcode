class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        
        while stack or curr:
            # Go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # Move to right subtree
            curr = curr.right