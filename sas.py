class Solution:
    def subsetXORSum(self, nums):
        self.total = 0

        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            # Include nums[index]
            dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index]
            dfs(index + 1, current_xor)

        dfs(0, 0)
        return self.total
