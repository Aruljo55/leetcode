class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
            
        # First pass to find potential candidates
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Second pass to verify candidates
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
                
        result = []
        threshold = len(nums) // 3
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
            
        return result