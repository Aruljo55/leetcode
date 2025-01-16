class Solution:
    def xorAllNums(self, nums1, nums2):
        xor_sum = 0
        
        # Iterate through each number in nums1
        for num1 in nums1:
            # Iterate through each number in nums2
            for num2 in nums2:
                xor_sum ^= num1 ^ num2  # XOR operation between num1 and num2
        
        return xor_sum
