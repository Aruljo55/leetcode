class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA

    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left

    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = None

        for bucket in buckets:
            if bucket[0] is None:
                continue
            if prev_max is not None:
                max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

        return max_gap
