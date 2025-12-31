class Solution:
    def maxAbsoluteSum(self, nums):
        max_sum = min_sum = 0
        curr_max = curr_min = 0
        
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, abs(min_sum))
    
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False
    
    def diffWaysToCompute(self, expression):
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        return results

# Example usage:
sol = Solution()
nums1 = [1,-3,2,3,-4]
nums2 = [2,-5,1,-4,3,-2]
print(sol.maxAbsoluteSum(nums1))  # Output: 5
print(sol.maxAbsoluteSum(nums2))  # Output: 8

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target1 = 5
target2 = 20
print(sol.searchMatrix(matrix, target1))  # Output: True
print(sol.searchMatrix(matrix, target2))  # Output: False

expression1 = "2-1-1"
expression2 = "2*3-4*5"
print(sol.diffWaysToCompute(expression1))  # Output: [0, 2]
print(sol.diffWaysToCompute(expression2))  # Output: [-34, -14, -10, -10, 10]