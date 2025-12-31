# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N,"
        
        # Preorder traversal (root, left, right)
        result = str(root.val) + ","
        result += self.serialize(root.left)
        result += self.serialize(root.right)
        
        return result
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Create a list from the serialized string
        values = data.split(',')
        self.index = 0
        
        def dfs():
            if self.index >= len(values) or values[self.index] == "N":
                self.index += 1
                return None
            
            # Create new node with current value
            node = TreeNode(int(values[self.index]))
            self.index += 1
            
            # Recursively build left and right subtrees
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()