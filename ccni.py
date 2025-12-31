class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        from collections import deque

        count = 0
        queue = deque([""])  # Start with empty prefix

        while queue:
            prefix = queue.popleft()
            candidate_str = prefix + s
            candidate_int = int(candidate_str)

            if candidate_int > finish:
                continue

            if candidate_int >= start:
                count += 1

            for d in range(0 if prefix else 1, limit + 1):  # avoid leading zeros
                queue.append(prefix + str(d))

        return count
