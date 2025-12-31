class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start, combination, target):
            if len(combination) == k and target == 0:
                result.append(combination[:])
                return

            for num in range(start, 10):
                if num > target:
                    break
                combination.append(num)
                backtrack(num + 1, combination, target - num)
                combination.pop()

        backtrack(1, [], n)
        return result

# Examples
solution = Solution()
print(solution.combinationSum3(3, 7))  # Output: [[1, 2, 4]]
print(solution.combinationSum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
print(solution.combinationSum3(4, 1))  # Output: []
