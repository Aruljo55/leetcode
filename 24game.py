class Solution:
    def judgePoint24(self, cards):
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for v in (
                            nums[i] + nums[j],
                            nums[i] - nums[j],
                            nums[i] * nums[j],
                        ):
                            if dfs(rest + [v]):
                                return True
                        if abs(nums[j]) > 1e-6:
                            if dfs(rest + [nums[i] / nums[j]]):
                                return True
            return False

        return dfs([float(x) for x in cards])
