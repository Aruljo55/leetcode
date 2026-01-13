from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(level)

        return result
