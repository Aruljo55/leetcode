from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        best = 1
        maxsum = root.val

        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > maxsum:
                maxsum = s
                best = level
            level += 1

        return best
