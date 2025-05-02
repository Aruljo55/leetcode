from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            dq = deque()
            j = len(workers) - 1
            p = pills

            for i in reversed(range(k)):
                while j >= len(workers) - k and workers[j] + strength >= tasks[i]:
                    dq.appendleft(workers[j])
                    j -= 1

                if dq and dq[-1] >= tasks[i]:
                    dq.pop()
                elif dq and p > 0:
                    dq.popleft()
                    p -= 1
                else:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
