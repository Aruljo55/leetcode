class Solution:
    def binaryTreePaths(self, root):
        def dfs(node, path, result):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                path += '->'
                dfs(node.left, path, result)
                dfs(node.right, path, result)
        
        result = []
        dfs(root, '', result)
        return result