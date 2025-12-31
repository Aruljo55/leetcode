class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        def buildTree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
                
            # Create root node from first element of preorder
            root = TreeNode(preorder[pre_start])
            
            # If only one node left
            if pre_start == pre_end:
                return root
                
            # Find the left child value in postorder
            left_val = preorder[pre_start + 1]
            left_idx = post_start
            while postorder[left_idx] != left_val:
                left_idx += 1
                
            # Calculate size of left subtree
            left_size = left_idx - post_start + 1
            
            # Recursively build left and right subtrees
            root.left = buildTree(
                pre_start + 1,
                pre_start + left_size,
                post_start,
                left_idx
            )
            
            root.right = buildTree(
                pre_start + left_size + 1,
                pre_end,
                left_idx + 1,
                post_end - 1
            )
            
            return root
            
        return buildTree(0, len(preorder) - 1, 0, len(postorder) - 1)