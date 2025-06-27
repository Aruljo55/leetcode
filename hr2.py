class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this_node, not_rob_this_node)

            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we can't rob its children
            rob = node.val + left[1] + right[1]

            # If we don't rob this node, we can choose to rob or not rob children
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))
