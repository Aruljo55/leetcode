class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            direction = nums[i] > 0

            while True:
                # Move slow once
                next_slow = next_index(slow)
                # Move fast twice
                next_fast = next_index(fast)
                next_fast2 = next_index(next_fast)

                # Direction check
                if (
                    nums[next_slow] == 0 or
                    nums[next_fast] == 0 or
                    nums[next_fast2] == 0 or
                    (nums[next_slow] > 0) != direction or
                    (nums[next_fast] > 0) != direction or
                    (nums[next_fast2] > 0) != direction
                ):
                    break

                slow = next_slow
                fast = next_fast2

                if slow == fast:
                    # Check cycle length > 1
                    if slow == next_index(slow):
                        break
                    return True

            # Mark visited path as 0
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                next_j = next_index(j)
                nums[j] = 0
                j = next_j

        return False
