class Solution:
    def recoverTree(self, root):
        # Initialize variables to store the nodes to be swapped and their predecessors
        x = y = pred = prev = None
        
        # Morris In-order Traversal
        while root:
            if root.left:
                # Find the inorder predecessor of the current node
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                
                # Create a temporary link to root
                if not pred.right:
                    pred.right = root
                    root = root.left
                else:
                    # Revert the changes
                    pred.right = None
                    # Check the swapped nodes
                    if prev and root.val < prev.val:
                        y = root
                        if not x:
                            x = prev
                    prev = root
                    root = root.right
            else:
                # Check the swapped nodes
                if prev and root.val < prev.val:
                    y = root
                    if not x:
                        x = prev
                prev = root
                root = root.right
        
        # Swap the values of the two nodes
        x.val, y.val = y.val, x.val
