from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator: sorts based on which concatenation gives a larger result
        def compare(x, y):
            return (x + y > y + x) - (x + y < y + x)  # Equivalent to cmp() in Python 2
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare), reverse=True)
        
        # Join sorted numbers
        result = ''.join(nums)
        
        # Edge case: If all numbers are zero, return "0" instead of "000..."
        return '0' if result[0] == '0' else result

# Example test cases
solution = Solution()
print(solution.largestNumber([10, 2]))        # Output: "210"
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"
print(solution.largestNumber([0, 0]))         # Output: "0"
