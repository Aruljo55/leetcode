class Solution:
    def minOperations(self, nums, k):
        # If any number is less than k, we cannot increase it
        if any(num < k for num in nums):
            return -1
        
        # Unique values strictly greater than k
        distinct_above_k = set(num for num in nums if num > k)
        
        # Number of operations = number of distinct values above k
        return len(distinct_above_k)
