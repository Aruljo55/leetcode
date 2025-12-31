class Solution:
    def maximumSum(self, nums):
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        digit_map = {}
        max_sum = -1
        
        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_map:
                max_sum = max(max_sum, num + digit_map[d_sum])
                digit_map[d_sum] = max(digit_map[d_sum], num)
            else:
                digit_map[d_sum] = num
        
        return max_sum
