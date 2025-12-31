class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = [num for num in nums if num != 0] + [0] * nums.count(0)
        return result

    def addOperators(self, num, target):
        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            for i in range(index + 1, len(num) + 1):
                temp = num[index:i]
                if len(temp) > 1 and temp[0] == '0':
                    continue
                curr = int(temp)
                if index == 0:
                    dfs(i, temp, curr, curr)
                else:
                    dfs(i, path + '+' + temp, value + curr, curr)
                    dfs(i, path + '-' + temp, value - curr, -curr)
                    dfs(i, path + '*' + temp, value - prev + prev * curr, prev * curr)
        result = []
        dfs(0, '', 0, 0)
        return result

# Example Usage
# sol = Solution()
# print(sol.addOperators("123", 6))  # Output: ["1*2*3", "1+2+3"]