import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        prev = list(range(-1, n - 1))
        next = list(range(1, n + 1))
        next[-1] = -1

        alive = [True] * n

        # count bad adjacent pairs
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            pair_sum, i = heapq.heappop(heap)

            j = next[i]
            if j == -1 or not alive[i] or not alive[j]:
                continue

            # remove old bad relations
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if next[j] != -1 and nums[j] > nums[next[j]]:
                bad -= 1

            # merge i and j
            nums[i] += nums[j]
            alive[j] = False

            nxt = next[j]
            next[i] = nxt
            if nxt != -1:
                prev[nxt] = i

            # add new bad relations
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad += 1
            if nxt != -1 and nums[i] > nums[nxt]:
                bad += 1

            if nxt != -1:
                heapq.heappush(heap, (nums[i] + nums[nxt], i))

            ops += 1

        return ops
