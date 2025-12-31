class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Parse the traversal string into (depth, value) pairs
        nodes = []
        i = 0
        while i < len(traversal):
            # Count dashes to determine depth
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Parse the number
            num = 0
            while i < len(traversal) and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            
            nodes.append((depth, num))
        
        # Stack to keep track of nodes at different depths
        stack = []
        
        # Create root node
        root = TreeNode(nodes[0][1])
        stack.append((0, root))
        
        # Process remaining nodes
        for i in range(1, len(nodes)):
            depth, value = nodes[i]
            node = TreeNode(value)
            
            # Pop nodes from stack until we find the parent
            while stack and stack[-1][0] >= depth:
                stack.pop()
            
            # The node at top of stack is the parent
            parent = stack[-1][1]
            
            # Add as left or right child
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            
            stack.append((depth, node))
        
        return root

