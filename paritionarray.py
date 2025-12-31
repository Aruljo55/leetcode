class Solution:
    def pivotArray(self, nums, pivot):
        less = []
        equal = []
        greater = []
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
                
        return less + equal + greater

solution = Solution()
print(solution.pivotArray([9,12,5,10,14,3,10], 10))
print(solution.pivotArray([-3,4,3,2], 2))